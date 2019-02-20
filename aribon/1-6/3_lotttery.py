#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

def gen_problem(n, m_is_sum):
    k = np.random.randint(n**2/2, size=n)
    if m_is_sum:
        m = np.sum(np.random.randint(n**2/2, size=4))
        return k, m
    else:
        return k, m

def can_be_sum_1(n, m, k):
    for i in range(0, n):
        current_sum = k[i]
        if current_sum > m:
            continue
        for j in range(0, n):
            current_sum = k[i] + k[j]
            if current_sum > m:
                continue
            for u in range(0, n):
                current_sum = k[i] + k[j] + k[u]
                if current_sum > m:
                    continue
                for v in range(0, n):
                    if k[i] + k[j] + k[u] + k[v] == m:
                        return True, [k[i] , k[j] , k[u] , k[v]]

    return False, []

# 最後の値となりうるものが配列中にあるかを探す
def can_be_sum_2(n, m, k):
    k_sorted = sorted(k)
    for i in range(0, n):
        current_sum = k_sorted[i]
        if current_sum > m:
            continue
        for j in range(0, n):
            current_sum = k_sorted[i] + k_sorted[j]
            if current_sum > m:
                continue
            for u in range(0, n):
                current_sum = k_sorted[i] + k_sorted[j] + k_sorted[u]
                if current_sum > m:
                    continue
                val_remain = m - current_sum
                if val_remain in k:
                    return True, [k[i] , k[j] , k[u] , val_remain]

    return False, []

def can_be_sum_3(n, m, k):
    k_sorted = sorted(k)
    combi_sums = np.zeros()
    for i in range(0, n):
        for j in range(i, n):


    return False, []

def check_result(n, m, k, out):
    [m_is_sum, k_for_m] = can_be_sum_3(n, m, k)
    if m_is_sum == out:
        print("OK", k_for_m, m)
    else:
        print("Not OK.", k_for_m, m)

if __name__ == '__main__':
    n = 3
    m = 10
    k = [1, 3, 5]
    out = True
    check_result(n, m, k, out)

    n = 3
    m = 9
    k = [1, 3, 5]
    out = False
    check_result(n, m, k, out)

    n = 500
    out = True
    k, m = gen_problem(n, out)
    check_result(n, m, k, out)

