#!/usr/bin/env python
# -*- coding:utf-8 -*-


def can_triangle(a, i, j, k):
    if a[i] + a[j] > a[k]:
        return True
    return False

def get_max_perimeter(n, a):
    a_sort = sorted(a)
    max_perimeter = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if can_triangle(a_sort, i, j, k):
                    perimeter = a_sort[i] + a_sort[j] + a_sort[k]
                    if max_perimeter < perimeter:
                        max_perimeter = perimeter
    return max_perimeter

def check_result(n, a, out):
    max_perimeter = get_max_perimeter(n, a)
    if max_perimeter == out:
        print("OK")
    else:
        print("Not OK")
        print("max_perimeter : ", max_perimeter)
if __name__ == '__main__':
    n = 5
    a = {2, 3, 4, 5, 10}
    out = 12
    check_result(n, a, out)

    n = 4
    a = {4, 5, 10, 20}
    out = 0
    check_result(n, a, out)