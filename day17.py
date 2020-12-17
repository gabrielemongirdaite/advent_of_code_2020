import numpy as np
import itertools
import copy
import time
import pandas as pd

df = pd.read_fwf('input_d17.txt', header=None)
l = df.loc[:, 0].tolist()

df_3 = np.zeros((20, 20, 20))

y = 14
for i in l:
    x = 7
    for j in i:
        if j == '#':
            df_3[x,y,14] = 1
        x += 1
    y -=1

def find_neighbours(x,y,z):
    change = [1, 0, -1]
    x_new = [x+i for i in change]
    y_new = [y+i for i in change]
    z_new = [z+i for i in change]
    n = list(itertools.product(x_new, y_new, z_new))
    n.pop(n.index((x,y,z)))
    return n


def cycle(df):
    df_new = copy.deepcopy(df)
    for i in np.argwhere(df >= 0):
        sum_neighbour = 0
        for neighbour in find_neighbours(i[0], i[1], i[2]):
            try:
                sum_neighbour += df[neighbour]
            except:
                pass
        if df[i[0], i[1], i[2]] == 1 and 2 <= sum_neighbour <= 3:
            df_new[i[0], i[1], i[2]] = 1
        elif df[i[0], i[1], i[2]] == 1:
            df_new[i[0], i[1], i[2]] = 0
        elif df[i[0], i[1], i[2]] == 0 and sum_neighbour == 3:
            df_new[i[0], i[1], i[2]] = 1
        else:
            df_new[i[0], i[1], i[2]] = 0
    return df_new

start_time = time.time()
df_after_1 = cycle(df_3)
df_after_2 = cycle(df_after_1)
df_after_3 = cycle(df_after_2)
df_after_4 = cycle(df_after_3)
df_after_5 = cycle(df_after_4)
df_after_6 = cycle(df_after_5)

print('1st part answer: ', len(np.transpose(np.nonzero(df_after_6))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))




