import pandas as pd
import numpy as np
import time


def world(action, value, S_N_sum, E_W_sum):
    if action == 'N':
        S_N_sum -= value
    elif action == 'S':
        S_N_sum += value
    elif action == 'W':
        E_W_sum -= value
    elif action == 'E':
        E_W_sum += value
    return S_N_sum, E_W_sum


def new_index(current_index, rot_int, degrees_int, len_lst):
    possible_ind = (current_index + rot_int * degrees_int)
    new_indx = possible_ind if abs(possible_ind) < len_lst else possible_ind % (len_lst - 1) - 1
    return new_indx

def rotation(current_position, rot, degrees):
    rot_int = 1 if rot == 'R' else -1
    degrees_int = degrees//90
    lst = ['E', 'S', 'W', 'N']
    current_index = lst.index(current_position)
    new_indx = new_index(current_index, rot_int, degrees_int, len(lst))
    return lst[new_indx]

def rotation_waypoint(E_W_waypoint, S_N_waypoint, rot, degrees):
    rot_int = 1 if rot == 'R' else -1
    degrees_int = degrees // 90
    if degrees_int % 2 != 0:
        if (degrees_int == 1 and rot_int == 1) or (degrees_int == 3 and rot_int == -1):
            S_N_waypoint_new = E_W_waypoint
            E_W_waypoint_new = -S_N_waypoint
        elif (degrees_int == 3 and rot_int == 1) or (degrees_int == 1 and rot_int == -1):
            S_N_waypoint_new = -E_W_waypoint
            E_W_waypoint_new = S_N_waypoint
    else:
        E_W_waypoint_new = E_W_waypoint * (-1)
        S_N_waypoint_new = S_N_waypoint * (-1)
    return E_W_waypoint_new, S_N_waypoint_new

def find_ship(lst):
    starting_position = 'E'
    E_W_sum = 0
    S_N_sum = 0
    for i in lst:
        action = i[0]
        if action in ('N', 'S', 'E', 'W'):
            S_N_sum, E_W_sum = world(action, int(i[1:]), S_N_sum, E_W_sum)
        elif action == 'F':
            S_N_sum, E_W_sum = world(starting_position, int(i[1:]), S_N_sum, E_W_sum)
        else:
            starting_position = rotation(starting_position, action, int(i[1:]))
    return E_W_sum, S_N_sum


start_time = time.time()
df = pd.read_fwf('input_d12.txt', header=None)
l = df.loc[:, 0].tolist()
print('1st part answer: ' + str(abs(find_ship(l)[0])+abs(find_ship(l)[1])))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

def find_ship_part_two(lst):
    E_W_waypoint = 10
    S_N_waypoint = -1
    E_W_sum = 0
    S_N_sum = 0
    for i in lst:
        action = i[0]
        if action in ('N', 'S', 'E', 'W'):
            S_N_waypoint, E_W_waypoint = world(action, int(i[1:]), S_N_waypoint, E_W_waypoint)
        elif action == 'F':
            S_N_sum += S_N_waypoint*int(i[1:])
            E_W_sum += E_W_waypoint*int(i[1:])
        else:
            E_W_waypoint, S_N_waypoint = rotation_waypoint(E_W_waypoint, S_N_waypoint, action, int(i[1:]))
    return E_W_sum, S_N_sum

start_time = time.time()
df = pd.read_fwf('input_d12.txt', header=None)
l = df.loc[:, 0].tolist()
print('2nd part answer: ' + str(abs(find_ship_part_two(l)[0])+abs(find_ship_part_two(l)[1])))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))