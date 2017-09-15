'''Adjusted Body Weight Chart Demo'''

import matplotlib.pyplot as plt


def calc_ideal_body_wt(inches):
    return 0.454545 * (105 + (5 * abs(60 - inches)))


def calc_adj_body_wt(inches, body_weight):
    ideal_body_wt = calc_ideal_body_wt(inches)
    adj_body_wt = (0.25 * (body_weight - ideal_body_wt)) + ideal_body_wt
    return adj_body_wt


def get_axis_bounds(x, y):
    return [min(x), max(x), min(y), max(y)]


def list2d(rows, columns):
    return [[0 for x in range(rows)] for y in range(columns)]

if __name__ == '__main__':
    body_weight = range(105, 351)  # 105 to 350 pounds, 1lb interval
    body_height = range(60, 85)    # 60 to 84 inches (5' to 7'), 1 in interval

    # set up the plot
    nx = len(body_weight)
    ny = len(body_height)
    z = list2d(nx, ny)

    # Itterate over the x, y planes and calculate the adjusted body weight
    for xi in xrange(nx):
        for yi in xrange(ny):
            z[yi][xi] = calc_adj_body_wt(body_height[yi], body_weight[xi])

    # Choose a color map from https://matplotlib.org/users/colormaps.html
    cs = plt.contour(body_weight, body_height, z, 20, cmap='binary')
    plt.clabel(cs, inline=1, fontsize=10, color='black')

    plt.annotate(
        'Ideal Body Weight',
        xy=(139, 65),
        xytext=(155, 63),
        zorder=10,
        arrowprops={
            'facecolor': 'black',
            'width': 2,
            'headwidth': 7
        },
    )

    ideal_body_wt = []
    for height in body_height:
        ideal_body_wt.append(calc_ideal_body_wt(height) * 2.2)
    plt.scatter(ideal_body_wt, body_height)

    plt.title('Adjusted Body Weight (adjBW) in lbs')
    plt.xlabel('Body Weight (lbs)')
    plt.ylabel('Body Height (in)')

    bounds = get_axis_bounds(body_weight, body_height)
    plt.xticks(range(bounds[0], bounds[1], 20))
    plt.yticks(range(bounds[2], bounds[3], 2))
    plt.axis(bounds)

    plt.grid(True)
    plt.savefig('adjust-body-weight.png', bbox_inches='tight', dpi=300)

    plt.show()
