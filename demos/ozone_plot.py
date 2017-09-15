import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.seterr(invalid='ignore')

FILENAME = 'mtmet_ozone_sept_2017.csv'

data = {}
data_units = {}
data_idx = {}
header = []


# === Read in CSV data ================================================================================================
row_count = -1  # why -1?
with open(FILENAME, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row_count += 1

        # Skip the header comments
        if row_count <= 5:
            header.append(row)
            continue

        # Get the column headers
        if row_count == 6:
            for idx in xrange(len(row)):
                data[row[idx]] = []
                data_idx[idx] = row[idx]
            continue

        # Grab the units
        if row_count == 7:
            for idx in xrange(len(row)):
                data_units[idx] = row[idx]
            continue

        # From here on till the end of the file we can just process the data
        for idx in xrange(len(row)):
            # Do we even have data to work with?
            if row[2] == '':
                continue

            # Basic case that works, but lets be smart about it. It would be nice to have a validator that can
            # check the units and change the value for us.
            # data[data_idx[idx]].append(row[idx])
            if data_idx[idx] == 'Date_Time':
                data[data_idx[idx]].append(datetime.datetime.strptime(row[idx], '%Y-%m-%dT%H:%M:%SZ'))
            elif data_units[idx] != '':
                data[data_idx[idx]].append(float(row[idx]))
            else:
                data[data_idx[idx]].append(row[idx])


# === Prepare Data ====================================================================================================
# Now we have all the data ready to go
# Find the start and end times for our average, then calculate the mean for the rolling average
time_delta = datetime.timedelta(hours=4)
period_start_time = data['Date_Time'][0] + time_delta
period_end_time = data['Date_Time'][-1] - time_delta
n_profiles = len(data['Date_Time'])
# print period_start_time, period_end_time

print '-- Some information about the data read in --'
print 'rows', row_count, n_profiles
print 'idx', data_idx
print 'units', data_units

rolling_average = [None] * n_profiles
for idx in xrange(n_profiles):
    if data['Date_Time'][idx] > period_start_time and data['Date_Time'][idx] < period_end_time:
        rolling_average[idx] = np.mean(data['ozone_concentration_set_1'][idx - 48: idx + 48])

# Do some NumPy stuff
np_ozone_ave = np.array(rolling_average, dtype=np.float)
np_ozone_val = np.array(np_ozone_ave, dtype=np.float)
np_datetime = np.array(data['Date_Time'])


# === Plot the image ==================================================================================================
fig, ax = plt.subplots(figsize=(10, 4))

# https://matplotlib.org/users/tight_layout_guide.html
plt.tight_layout()

# !! Be sure to walk them thru this.
# print header
station_name = header[1][0].split(': ')[1]
# start_date = datetime.datetime.strftime(np.min(np_datetime), '%m-%d-%y')  # the overly complex way
start_date = np.min(np_datetime).strftime('%m-%d')  # >? the much simpler way, but why?
start_year = np.min(np_datetime).strftime('%Y')
end_date = np.max(np_datetime).strftime('%m-%d')
# print station_name, start_date
# exit()

plt.title('Ozone Measurements at %s for %s - %s %s' % (station_name, start_date, end_date, start_year))

# Plot the measurements
# https://matplotlib.org/api/lines_api.html
# https://matplotlib.org/examples/pylab_examples/set_and_get.html
plt.plot(
    data['Date_Time'],
    data['ozone_concentration_set_1'],
    color='0.75',
    linestyle='None',
    marker='o',
    markersize=2,
    zorder=1,
    label='Ozone Concentration'
)

# Add the rolling average to the figure
plt.plot(data['Date_Time'], rolling_average, zorder=4, label='8hr Rolling Average')
x_format = mdates.DateFormatter('%m-%d-%y')
ax.xaxis.set_major_formatter(x_format)

# Add the 'over 70 ppb' indicators
over_70_idx = np.where((np.isfinite(np_ozone_ave)) & (np_ozone_ave > 70))
plt.axhline(y=70, color='r', linestyle='--', zorder=3, label='70 ppb Threshold')

# Refactor lesson, now we just want to change the color of the line to red, which makes the plot loot a lot nicer.
# plt.scatter(np_datetime[over_70_idx], np_ozone_ave[over_70_idx], zorder=4, color='r')
# https://matplotlib.org/examples/pylab_examples/nan_test.html
_y = np_ozone_ave.copy()
_y[np_ozone_ave < 70] = np.nan
plt.plot(np_datetime, _y, zorder=5, color='r', linestyle='-', linewidth=3, solid_capstyle='round')

fig.autofmt_xdate()

# https://matplotlib.org/users/legend_guide.html
l = plt.legend(loc=1)
l.set_zorder(20)  # place the ledgend on the top layer

# https://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.savefig
plt.savefig('ozone-figure.svg', format='svg')
plt.show()
