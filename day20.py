import pandas as pd
import numpy as np
import re
import time


def flip(x, y):
    return (x, 9-y)


def rotate(x_left, y_left):
    coord = []
    coord.append((x_left, y_left))
    coord.append((9-y_left, x_left))
    coord.append((9, 9-y_left))
    coord.append((y_left, 9))
    return coord


start_time = time.time()
df = pd.read_fwf('input_d20.txt', header=None)
l = df.loc[:, 0].tolist()

i = 0
dct = {}
while i < len(l)-10:
    if l[i][0:4] == 'Tile':
        tile = []
        for j in range(i+1, i+11):
            tile.append(l[j])
        dct[l[i][5:]] = tile
    i += 11

dct2 = {}
for i in dct:
    coord_l = [[], [], [], []]
    coord_l_f = [[], [], [], []]
    coord_r = [[], [], [], []]
    coord_r_f = [[], [], [], []]
    coord_u = [[], [], [], []]
    coord_u_f = [[], [], [], []]
    coord_d = [[], [], [], []]
    coord_d_f = [[], [], [], []]
    for k, j in enumerate(dct[i]):
        if j[0] == '#':
            [coord_l[l[0]].append(rotate(0, k)[l[0]]) for l in enumerate(coord_l)]
            coord_l = [sorted(coord_l[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_l)]
            x, y = flip(0, k)
            [coord_l_f[l[0]].append(rotate(x, y)[l[0]]) for l in enumerate(coord_l_f)]
            coord_l_f = [sorted(coord_l_f[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_l_f)]
        if j[9] == '#':
            [coord_r[l[0]].append(rotate(0, 9-k)[l[0]]) for l in enumerate(coord_r)]
            coord_r = [sorted(coord_r[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_r)]
            x, y = flip(0, 9-k)
            [coord_r_f[l[0]].append(rotate(x, y)[l[0]]) for l in enumerate(coord_r_f)]
            coord_r_f = [sorted(coord_r_f[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_r_f)]
    for k, j in enumerate(dct[i][0]):
        if j == '#':
            [coord_u[l[0]].append(rotate(0, 9 - k)[l[0]]) for l in enumerate(coord_u)]
            coord_u = [sorted(coord_u[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_u)]
            x, y = flip(0, 9 - k)
            [coord_u_f[l[0]].append(rotate(x, y)[l[0]]) for l in enumerate(coord_u_f)]
            coord_u_f = [sorted(coord_u_f[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_u_f)]
    for k, j in enumerate(dct[i][9]):
        if j == '#':
            [coord_d[l[0]].append(rotate(0, k)[l[0]]) for l in enumerate(coord_d)]
            coord_d = [sorted(coord_d[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_d)]
            x, y = flip(0, k)
            [coord_d_f[l[0]].append(rotate(x, y)[l[0]]) for l in enumerate(coord_d_f)]
            coord_d_f = [sorted(coord_d_f[l[0]], key=lambda tup: (tup[0], tup[1])) for l in enumerate(coord_d_f)]
    answer = []
    answer.extend(coord_l + coord_r + coord_u + coord_d + coord_l_f  + coord_r_f  \
                         + coord_u_f  + coord_d_f )
    dct2[i] = answer


dct3 ={}
for i in dct2:
    cnt = ''
    for j in dct2[i]:
        for k in dct2:
            if j in dct2[k] and i != k:
                cnt += str(k)+' '
    dct3[i] = cnt

mlt = 1
for i in dct3:
    if len(set(re.findall(r'\b\d+\b', dct3[i]))) == 2:
        mlt *= int(re.findall(r'\b\d+\b', i)[0])


print('1st part answer: ', mlt)
print("--- %s seconds for 1st part---" % (time.time() - start_time))
# 13224049461431