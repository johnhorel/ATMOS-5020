'''Dew Point Temperature Chart Demo'''

import matplotlib.pyplot as plt
from matplotlib import ticker


def get_axis_bounds(x, y, margin=0):
    '''Returns the boundries of a 2D list'''
    return [min(x) - margin, max(x) + margin, min(y) - margin, max(y) + margin]


def list2d(rows, columns):
    '''Returns a 2D list'''
    return [[0 for x in range(rows)] for y in range(columns)]


def calc_dew_point_temp(air_temp, rel_hum):
    '''
    Calculates Dew Point Temperature (DPT) in degrees C
        Hydrology: Water Quantity and Quality Control, 2nd Edition
        Martin P. Wanielista, Robert Kersten, Ron Eaglin
        ISBN: 978-0-471-07259-1
    '''
    return ((rel_hum / 100.0)**0.125) * (112.0 + 0.9 * air_temp) + 0.1 * air_temp - 112.0


def FtoC(temperature):
    '''Converts Fahrenheit to Celsius'''
    return (float(temperature) - 32.0) / 1.8


def CtoF(temperature):
    '''Converts Celsius to Fahrenheit'''
    return float(temperature) * 1.8 + 32


if __name__ == '__main__':
    air_temperature = range(-60, 60)  # from range check
    relative_humidity = range(0, 100)

    # Define the lists that will be used to render the contour plot
    nx = len(air_temperature)
    ny = len(relative_humidity)
    z = list2d(nx, ny)

    # Itterate over the x, y planes and calculate the dew point temperature
    for xi in xrange(nx):
        for yi in xrange(ny):
            z[yi][xi] = calc_dew_point_temp(air_temperature[xi], relative_humidity[yi])

    # We'll use this later too
    bounds = get_axis_bounds(air_temperature, relative_humidity)

    # Choose a color map from https://matplotlib.org/users/colormaps.html
    csx = plt.contourf(air_temperature, relative_humidity, z, 32, cmap='jet')
    cs = plt.contour(air_temperature, relative_humidity, z, 20, linewidths=1, colors='k')

    # Explain this sugar!
    r = range(bounds[0], bounds[1], 11)
    label_loc = list(((i, 50) for i in r))

    contour_labels = plt.clabel(cs, inline=True, colors='k', fmt='%d', manual=label_loc, fontsize=14)

    for l in contour_labels:
        l.set_rotation(0)

    # https://stackoverflow.com/a/34353493
    for line in cs.collections:
        line.set_linestyle('-')
    #     if line.get_linestyle() == [(None, None)]:
    #         pass
    #     else:
    #         # line.set_color('red')
    #         pass

    # https://stackoverflow.com/questions/22012096/how-to-set-number-of-ticks-in-plt-colorbar
    cbar = plt.colorbar(csx)
    cbar.locator = ticker.MaxNLocator(nbins=20)
    cbar.update_ticks()
    cbar.ax.set_ylabel('Dew Point Temperature (C)', labelpad=10)

    plt.title('Dew Point Temperature Chart')
    plt.xlabel('Air Temperature (C)')
    plt.ylabel('Relative Humidity (%)')

    plt.xticks(range(bounds[0], bounds[1], 10))
    plt.yticks(range(bounds[2], bounds[3], 5))
    plt.axis(bounds)

    plt.grid(True)
    plt.savefig('dew-point-chart.png', bbox_inches='tight', dpi=300)

    plt.show()
