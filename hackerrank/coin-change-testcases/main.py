#!/usr/bin/env python
# -*- coding:utf-8 -*-

# def getWays(n, c):
#     coin_sets = pickCoin(n, c, 0, [], [])
#     return coin_sets
#
# def pickCoin(n, c, cur_sum, cur_list, lists):
#     for coin in c:
#         print(coin)
#         print(cur_list)
#         if cur_sum + coin == n:
#             cur_list.append(coin)
#             cur_sum = cur_sum + coin
#             lists.append(cur_list)
#             cur_list = []
#             cur_sum = 0
#             return lists
#         elif cur_sum + coin < n:
#             cur_list.append(coin)
#             cur_sum = cur_sum + coin
#             # print(cur_sum)
#             lists = pickCoin(n, c, cur_sum, cur_list, lists)
#     return lists

def recur(a):
    val = a
    if val < 5:
        recur(val + 1)
    else:
        return val
    return val

if __name__ == '__main__':
    c = [1, 2, 3]
    n = 4
    # print(getWays(n, c))
    print(recur(0))


