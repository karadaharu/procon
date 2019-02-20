#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
def read_data():
    with open("2_lake_counting.txt", "r") as f_in:
        in_tmp = f_in.readline()
        n, m = [int(s) for s in in_tmp.rstrip().split()]
        yard = np.zeros((n, m))
        for i in range(0, n):
            line = f_in.readline()
            for j, p in enumerate(list(line.rstrip())):
                if p == 'W':
                    yard[i,j] = 1
    return yard

def count_lake():
    n_lake = 0
    for i in range(n):
        for j in range(m):
            lake_ind = m * i + j
            if yard[i,j] == 1 and lake_ind not in lake_indices:
                n_lake = n_lake + 1
                lake_indices.append(lake_ind)
                get_lake_shape(i,j)
    return n_lake

def get_lake_shape(i, j):
    neighbours = get_neighbours(i,j)
    for nb in neighbours:
        lake_ind = m * nb[0] + nb[1]
        if yard[nb[0], nb[1]] == 1 and lake_ind not in lake_indices:
            lake_indices.append(lake_ind)
            get_lake_shape(nb[0], nb[1])

def get_neighbours(i,j):
    dirs = [-1, 0, 1]
    neighbours = []
    for h in dirs:
        for v in dirs:
            if j + h >= 0 and j + h < m and i + v >= 0 and i + v < n and not (h == 0 and v == 0):
                neighbours.append([i + v, j + h])
    return neighbours
if __name__ == '__main__':
    yard = read_data()
    n = yard.shape[0]
    m = yard.shape[1]
    lake_indices = []
    n_lakes = count_lake()
    print(n_lakes)

