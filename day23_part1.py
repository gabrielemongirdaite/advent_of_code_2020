import time


cups = [3, 8, 9, 5, 4, 7, 6, 1, 2]
#cups = [3, 8,  9,  1,  2,  5,  4,  6,  7]


def find_index(idx, lst):
    if idx >= len(lst):
        new_idx = idx % (len(lst))
    elif idx < 0:
        new_idx = len(lst)+idx
    else:
        new_idx = idx
    return new_idx


def pick_up(current, lst):
    idx = lst.index(current)
    idx_1 = find_index(idx + 1, lst)
    idx_2 = find_index(idx + 2, lst)
    idx_3 = find_index(idx + 3, lst)
    return [lst[idx_1], lst[idx_2], lst[idx_3]]


def destination(current, lst, to_be_deleted):
    copy_lst = lst.copy()
    for i in to_be_deleted:
        try:
            copy_lst.remove(i)
        except:
            pass
    if current - 1 < min(copy_lst):
        dest = max(copy_lst)
    else:
        if current - 1 in copy_lst:
            dest = current - 1
        else:
            current = current - 1
            dest = destination(current, copy_lst, to_be_deleted)
    return dest


def new_structure(current, lst):
    pick_up_lst = pick_up(current, lst)
    dest_idx = lst.index(destination(current, lst, pick_up_lst))
    el_1, el_2, el_3 = pick_up_lst
    idx_3 = lst.index(el_3)
    i = find_index(idx_3 + 1, lst)
    lst_new = lst.copy()
    while find_index(i-1, lst) != dest_idx:
        lst_idx = find_index(i-3, lst)
        lst_new[lst_idx] = lst[i]
        new_dest_idx = lst_idx
        i = find_index(i+1, lst)
    for j in range(3):
        idx = find_index(new_dest_idx+1+j, lst)
        lst_new[idx] = pick_up_lst[j]
    return lst_new


start_time = time.time()
current = 3
for i in range(100):
    cups = new_structure(current, cups)
    current = cups[find_index(i+1, cups)]

print('1st part answer: ', cups)
print("--- %s seconds for 1st part---" % (time.time() - start_time))


