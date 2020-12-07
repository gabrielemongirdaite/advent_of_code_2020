import pandas as pd
import numpy as np
import time
import re
from collections import defaultdict


def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list =[sub.replace(' bags', '').replace(' bag', '').replace('.', '').split(' contain ') for sub in content_list]
    list_colors = []
    list_numbers = []
    for i in content_list:
        list_numbers.append([int(s) for s in i[1].split() if s.isdigit()])
        i[1] = re.sub(r'[0-9]+', ' ', i[1])
        i[1] = i[1].replace('  ', '').split(', ')
        list_colors.append(i[0])
    content_dict = {item[0]: item[1] if item[1] != ['no other'] else [item[0]] for item in content_list}
    return content_dict, list_colors, list_numbers


# idea taken from: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
def BFS(s, content_dict, list_colors):
    # Mark all the vertices as not visited
    queue_all = []
    visited = [False] * (len(content_dict) + 1)
    # Create a queue for BFS
    queue = []
    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    queue_all.append(s)
    visited[list_colors.index(s)] = True
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in content_dict[s]:
            if visited[list_colors.index(i)] == False:
                queue.append(i)
                queue_all.append(i)
                visited[list_colors.index(i)] = True
    return visited, queue_all


start_time = time.time()
dict_colors, lst_colors, list_numbers = read_file('input_d7.txt')
answer = 0
for i in lst_colors:
    answer += BFS(i, dict_colors, lst_colors)[0][lst_colors.index('shiny gold')]

print('1st part answer: ' + str(answer-1))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


# Idea taken from here: https://www.geeksforgeeks.org/find-paths-given-source-destination/
def printAllPathsUtil(u, d, visited, path, content_dict, list_colors):
    # Mark the current node as visited and store in path
    visited[list_colors.index(u)] = True
    path.append(u)
    # If current vertex is same as destination, then print
    # current path[]
    if u == d:
        multiplication_path = 1
        for i in path:
            try:
                multiplication_path *= list_numbers[list_colors.index(i)][content_dict[i].index(path[path.index(i)+1])]
            except:
                pass
        print(multiplication_path)
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in content_dict[u]:
            if visited[list_colors.index(i)] == False:
                printAllPathsUtil(i, d, visited, path, content_dict, list_colors)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[list_colors.index(u)] = False


def printAllPaths(s, d, content_dict, list_colors):

    # Mark all the vertices as not visited
    visited = [False] * (len(content_dict) + 1)

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    for i in set(lst_colors):
        if i != s:
            printAllPathsUtil(s, i, visited, path, content_dict, list_colors)


print('You have to sum all these numbers:')
printAllPaths('shiny gold', '', dict_colors, lst_colors)
