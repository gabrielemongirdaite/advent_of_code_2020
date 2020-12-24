import matplotlib.pyplot as plt
import math
from matplotlib.patches import RegularPolygon
import numpy as np


coord = [[0,0],[-1,1],[-2,0],[-1,-1],[1,-1],[2,0],[1,1]]
colors = [["Green"],["Blue"],["Yellow"],["Pink"],["Red"],["Grey"],["White"]]
labels = [['center'],['nw'], ['w'],['sw'],['se'],['e'], ['ne']]

# Horizontal cartesian coords
hcoord = [c[0]*np.sin(np.radians(120))/np.sin(np.radians(30))/3 for c in coord]


# Vertical cartersian coords
vcoord = [c[1]  for c in coord]
print(np.sin(np.radians(60)))
fig, ax = plt.subplots(1)
ax.set_aspect('equal')

# Add some coloured hexagons
for x, y, c, l in zip(hcoord, vcoord, colors, labels):
    color = c[0].lower()  # matplotlib understands lower case words for colours
    hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                         orientation=np.radians(0),
                         facecolor=color, alpha=0.2, edgecolor='k')
    ax.add_patch(hex)
    # Also add a text label
    ax.text(x, y+0.2, l[0], ha='center', va='center', size=20)

# Also add scatter points in hexagon centres
ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

plt.show()