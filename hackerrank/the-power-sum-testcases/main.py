#!/usr/bin/env python
# -*- coding:utf-8 -*-

def powerSum(i, sum):
    global X, N, n_combi
    sum_tmp = sum + i ** N
    if sum_tmp > X:
        return
    elif sum_tmp == X:
        n_combi = n_combi + 1
        return
    powerSum(i+1, sum)
    powerSum(i+1, sum + i ** N)

if __name__ == '__main__':
    X = 100
    N = 2
    n_combi = 0
    powerSum(1, 0)
    print(n_combi)