#!/usr/bin/env python
# -*- coding:utf-8 -*-

def formingMagicSquare(s):
    # sums = {"col": [0, 0, 0], "row":[0, 0, 0]}
    # for i in range(3):
    #     sums["col"][i] = sum([s[i][j] for j in range(3)])
    #     sums["row"][i] = sum(s[i])
    # cost = 0
    # for i in range(3):
    #     for j in range(3):
    #         if sums["col"][i] == sums["row"][j] and sums["col"][i] != 15:
    #             v_common = s[i][j]
    #             cost = cost + abs( 15 - sums["col"][i] )
    #             s[i][j] = s[i][j] + 15 - sums["col"][i]
    #             sums["col"][i] = 15
    #             sums["row"][j] = 15
    # return cost


if __name__ == '__main__':

    fin = open("./input/input22.txt", 'r')
    s = []

    for _ in range(3):
        in_str = fin.readline()
        s.append(list(map(int, in_str.rstrip().split())))
    result = formingMagicSquare(s)
    print(s)
    print(result)
