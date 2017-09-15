# Homework No. 4

## Objectives

- Demonstrate the ability to download data from the internet
- Parse retrieved data into a usable format
- Calculate a derived variable
- Visualize the data in the form of a 1D plot
- Clearly describe the visualization in a caption
- Display the final product as a webpage via your CHCP public folder

## Retrieve data to plot

You will need to download a CSV file from the Mesowest/SynopticLabs Mesonet service.  There is nothing you need to do to the URL, just use cURL to download it.  I highly recommend you name it something meaningful.

```
http://api.mesowest.net/v2/stations/timeseries?stid=mtmet&token=59f35e971f4f406ea8d873a2bf0600f3&start=201709110000&end=201709152359&vars=air_temp,relative_humidity&output=csv
```

## Parse retrieved data into a usable format

You will need to write a Python script to parse and visualize the data.  You can start with the following boiler plate.

```python
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.seterr(invalid='ignore')

def calc_dew_point_temp(air_temp, rel_hum):
    return 0


def FtoC(temperature):
    return (temperature - 32.0) / 1.8


def CtoF(temperature):
    return temperature * 1.8 + 32


if __name__ == '__main__':
    # Your code goes here
    print 'Hello World!'
```


Using the CSV parsing pattern discussed in class, you will be able to parse the downloaded CSV.

Please see [plotting ozone concentrations demo](ozone-demo).

## Calculate a derived variable

If you started the boilerplate code above, you will just need to edit the `calc_dew_point_temp` function.  Replace the `0` in `return 0` with an equation (or the calculated result) for dew point temperature.

_Hint_: The "Check Your Understanding" from September 20 has the equation for you.


## Visualize the data in the form of a 1D plot

Using the concepts presented in the [ozone concentrations demo](ozone-demo) and [dew point chart demo](dew-point-demo), you will need to re-create the following graphic.

![what you should have][expected-result]


The duel axis problem can be explained with the following:

```python
# === Prepare Data ===

# All of the arrays we will plot
date_time = np.arange(10)
air_temperature = np.random.random(10) * 30
relative_humidity = np.random.random(10) * 100 - 10
dew_point_temp = np.random.random(10) * 100 - 10


# === Plot the image ===
fig, ax = plt.subplots(figsize=(10, 5))

# BESURE TO READ THIS!!
# https://stackoverflow.com/a/5487005/4835631

plt.title('Way Crazy Weather!')

# Plot the air & dew point temperatures on the y1 axis
_l1 = ax.plot(date_time, air_temperature, color='m', label='Air Temperature')
_l2 = ax.plot(date_time, dew_point_temp, color='k', label='Dew Point Temperature')
ax.set_ylabel('Air & Dew Point Temperarures (C)', color='k')
ax.tick_params('y', colors='k')
ax.grid(True)

# Add the relative humidity to the y2 axis
# Need to create a duel axis plot, also known as a 'yyplot'
# https://matplotlib.org/examples/api/two_scales.html
ax2 = ax.twinx()
_l3 = plt.plot(date_time, relative_humidity, color='b', label='Relative Humidity')
ax2.set_ylabel('Relative Humidity', color='b')
ax2.tick_params('y', colors='b')
ax2.grid(True, linestyle='dashed')

# HINT HINT HINT, this code will fit perfectly under the
# if __name__ == '__main__': statement

# Make a legend, and put it below the figure
# http://matplotlib.org/users/legend_guide.html#plotting-guide-legend
# https://stackoverflow.com/a/5487005/4835631
lines = _l1 + _l2 + _l3
labels = [x.get_label() for x in lines]
fig.subplots_adjust(bottom=0.3)
lgd = ax.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.1))

# https://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.savefig
# plt.savefig('metvars-figure.svg', format='svg', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.show()
```

## Clearly describe the visualization in a caption

What good is a figure with no caption or explanation?  You'll need to copy [this page](website-template) to your CHPC `public_html` folder.  Then update the text to reflect your work.  Bonus points for those who add additional weather maps from the NWS or of the like and discuss the weather during the time period of your figure.

## Display the final product as a webpage via your CHCP public folder
**Please name the file `weather-report.html`** and be located in your `/5020/` folder.  I will not go looking for files anywhere else.

## Submitting your work

Working in a group to solve the problem is fine, but you are expected to write your own code.  You will also need to add a header to your python codes prior to submission that follow the pattern:

```python
'''
    Homework No. 4
    Visualizing Basic Meteorological Variables
    Adam C. Abernathy
    u0751826

    This program plots air temperature, dew point and relative humidity
    as a function of time.  Requires a CSV file from the Mesowest API
    using the following URL:

    http://api.mesowest.net/v2/stations/timeseries?
      stid=mtmet&token=59f35e971f4f406ea8d873a2bf0600f3&
      start=201709110000&end=201709152359&vars=air_temp,relative_humidity&
      output=csv

    and the output saved to "mtmet_at_rh_0911_0915.csv" in the end
    the result image is saved as "metvars-figure.svg".
'''
```

## Getting help

I am available to help up until about 9pm the night before the assignment is due.  When asking for help, please ask targeted questions, not just saying "it doesn't work".  80% of the battle with writing code is just understanding _where_ the problem is and _what_ might be causing it.




<!-- Refs -->
[ozone-demo]: //
[dew-point-demo]: //
[website-template]: //
[expected-result]: supplementary/metvars-figure.svg
