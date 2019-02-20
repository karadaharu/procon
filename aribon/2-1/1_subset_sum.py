#!/usr/bin/env python
# -*- coding:utf-8 -*-
def can_be_sum(i, sum):
    print(i, sum)
    if i == n:
        return sum == k
    if can_be_sum(i + 1, sum):
        return True
    if can_be_sum(i + 1, sum + a[i]):
        return True
    return False

if __name__ == '__main__':
    n = 4
    a = [1, 2, 4, 7]
    k = 13
    out = True
    if out == can_be_sum(0, 0):
        print("ok")