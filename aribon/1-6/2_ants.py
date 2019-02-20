#!/usr/bin/env python
# -*- coding:utf-8 -*-


def get_times(L, n, x):
    time = {"min": 0, "max": 0}
    # min : 近い方へ行くときの最大値
    # max : 遠い方へ行くときの最大値
    for pos in x:
        # どっちに近いか
        x_time ={\
                 "min" : min([pos, L - pos]),\
                 "max" : max([pos, L - pos])\
                 }
        for t in time.keys():
            if time[t] < x_time[t]:
                time[t] = x_time[t]
    return time

def check_result(L, n, x, out):
    time = get_times(L, n, x)
    is_ok = True
    for t in time.keys():
        if time[t] != out[t]:
            is_ok = False
            print("Not OK. Result:", time[t], ", Answer", out[t])
    if is_ok:
        print("OK")



if __name__ == '__main__':
    L = 10
    n = 3
    x = [2, 6, 7]
    out = {"min": 4, "max":8}

    check_result(L, n, x, out)