#!/usr/bin/env python
# -*- coding:utf-8 -*-

def sum(n):
    if n <= 0:
        return n
    return n + sum(n-1)

if __name__ == '__main__':
    print(sum(10))
