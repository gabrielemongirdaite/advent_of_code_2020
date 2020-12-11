import pandas as pd
import numpy as np
from collections import Counter
import time


def adjacant_cordinates(x,y, rows, cols, arr):
    return [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]


def first_seat(x, y, arr, y_direction, x_direction, n_rows, n_cols):
    i = 1
    try:
        while arr[y+y_direction*i][x+x_direction*i] not in ['L', '#']:
            if 0<=(y+y_direction*(i+1))<=n_rows and 0<=(x+x_direction*(i+1))<=n_cols:
                i += 1
            else:
                break
    except:
        pass
    return (x+x_direction*i, y+y_direction*i)


def adjacant_cordinates_any_seat(x,y, rows, cols, arr):
    return [first_seat(x, y, arr, 1, 0, rows, cols), first_seat(x, y, arr, 1, 1, rows, cols), first_seat(x, y, arr, 0, 1, rows, cols), first_seat(x, y, arr, -1, 1, rows, cols), first_seat(x, y, arr, -1, 0, rows, cols), first_seat(x, y, arr, -1, -1, rows, cols), first_seat(x, y, arr, 0, -1, rows, cols), first_seat(x, y, arr, 1, -1, rows, cols)]


def occupied_seats(arr, occupied, adj_cor, tolerance):
    n_cols = len(arr[0])
    n_rows = np.shape(arr)[0]
    occupied_cordinates = []
    unoccupied_cordinates = []
    for cols in range(n_cols):
        for rows in range(n_rows):
            seats = []
            for i in adj_cor(cols, rows, n_rows-1, n_cols-1, arr):
                try:
                    if i[0] >= 0 and i[1] >= 0: # not to allow negative coordinates (they are possible in arrays)
                        seats.append(arr[i[1]][i[0]])
                except:
                    pass
            seats_dict = Counter(seats)
            if arr[rows][cols] == "L" and not("#" in seats_dict):
                occupied += 1
                occupied_cordinates.append((cols, rows))
            elif arr[rows][cols] == "#" and seats_dict['#'] >= tolerance:
                occupied -= 1
                unoccupied_cordinates.append((cols, rows))
    return occupied, occupied_cordinates, unoccupied_cordinates


def redraw_seating_map(arr, occupied, unoccupied):
    for i in occupied:
        arr[i[1]][i[0]] = '#'
    for i in unoccupied:
        arr[i[1]][i[0]] = 'L'
    return arr


start_time = time.time()
df = pd.read_fwf('input_d11.txt', header=None)
l = df.loc[:, 0].tolist()
l = [list(c) for c in l]
l_array = np.array(l)


occupied_new, occupied_cordinates, unoccupied_cordinates = occupied_seats(l_array, 0, adjacant_cordinates, 4)
occupied_old = 0
arr = redraw_seating_map(l_array, occupied_cordinates, unoccupied_cordinates)
while occupied_new != occupied_old:
    occupied_old = occupied_new
    occupied_new, occupied_cordinates, unoccupied_cordinates = occupied_seats(arr, occupied_new, adjacant_cordinates, 4)
    arr = redraw_seating_map(arr, occupied_cordinates, unoccupied_cordinates)


print('1st part answer: ' + str(occupied_new))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
l_array = np.array(l)

occupied_new, occupied_cordinates, unoccupied_cordinates = occupied_seats(l_array, 0, adjacant_cordinates_any_seat,5)
occupied_old = 0
arr = redraw_seating_map(l_array, occupied_cordinates, unoccupied_cordinates)
while occupied_new != occupied_old:
    occupied_old = occupied_new
    occupied_new, occupied_cordinates, unoccupied_cordinates = occupied_seats(arr, occupied_new, adjacant_cordinates_any_seat,5)
    arr = redraw_seating_map(arr, occupied_cordinates, unoccupied_cordinates)

print('2nd part answer: ' + str(occupied_new))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))