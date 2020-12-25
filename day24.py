import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import pandas as pd
import time

print_graph = False

def north_west(x,y):
    return (x-1, y+1)


def west(x,y):
    return (x-2, y)


def south_west(x,y):
    return (x-1, y-1)


def south_east(x,y):
    return (x+1, y-1)


def east(x,y):
    return (x+2, y)


def north_east(x,y):
    return (x+1, y+1)


start_time = time.time()
possible_directions = ['nw', 'w', 'sw', 'se', 'e', 'ne']
current = (0,0)
coordinates = [(0,0)]
colors = [['White']]

df = pd.read_fwf('input_d24.txt', header=None)
l = df.loc[:, 0].tolist()

for ln in l:
    k = 0
    while len(ln)>0:
        k += 1
        direction = ln[0:2] if ln[0:2] in possible_directions else ln[0:1]
        if direction == 'nw':
            current = north_west(current[0], current[1])
        elif direction == 'w':
            current = west(current[0], current[1])
        elif direction == 'sw':
            current = south_west(current[0], current[1])
        elif direction == 'se':
            current = south_east(current[0], current[1])
        elif direction == 'e':
            current = east(current[0], current[1])
        elif direction == 'ne':
            current = north_east(current[0], current[1])

        if current not in coordinates:
            coordinates.append(current)
            colors.append(['White'])
        else:
            idx = [i for i, x in enumerate(coordinates) if x == current]
            col = colors[idx[0]]
            for i in idx:
                coordinates.pop(i)
                colors.pop(i)
            coordinates.append(current)
            colors.append(col)
        ln = ln[len(direction):]

    indices = [i for i, x in enumerate(coordinates) if x == coordinates[-1]]
    if colors[-1] == ['White']:
        for i in indices:
            colors[i] = ['Black']
    else:
        for i in indices:
            colors[i] = ['White']
    current = (0, 0)


print('1st part answer: ', len(set([y for x, y in zip(colors, coordinates) if x == ['Black']])))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

if print_graph:
    # Horizontal cartesian coords
    hcoord = [c[0]*np.sin(np.radians(120))/np.sin(np.radians(30))/3 for c in coordinates]


    # Vertical cartersian coords
    vcoord = [c[1]  for c in coordinates]
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Add some coloured hexagons
    for x, y, c in zip(hcoord, vcoord, colors):
        color = c[0].lower()  # matplotlib understands lower case words for colours
        hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                                         orientation=np.radians(0),
                                         facecolor=color, alpha=0.2, edgecolor='k')
        ax.add_patch(hex)


    # Also add scatter points in hexagon centres
    ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

    plt.show()


