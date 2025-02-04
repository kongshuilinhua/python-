'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-23 10:54:34
LastEditors: ElysiaRealme
Language: Python
'''
from io import BytesIO, IOBase
import sys
import os

# import time
import bisect
# import functools
import math
import random
# import re
from collections import Counter, defaultdict, deque
# from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import accumulate, combinations, permutations
# from operator import add, iand, ior, itemgetter, mul, xor
# from string import ascii_lowercase, ascii_uppercase
from typing import *

input = lambda: sys.stdin.readline().rstrip("\r\n")


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))


def GMI():
    return map(lambda x: int(x) - 1, input().split())


def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))


dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
inf = float('inf')

from bisect import *


class BIT:
    def __init__(self, n):
        self.tree = [0] * n  # 注意下标从1开始

    def lowbit(self, x):
        return x & (-x)

    # arr[i] += val
    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += self.lowbit(i)

    # 返回arr[:i+1]的sum
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res
# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# zkw线段树


# 题目：
# 多少个点包含A而不包含B
# 容斥的思想,包含A的数量-包含A且包含B的数量
n, q = MII()
N = int(2e5 + 10)
tree = BIT(N + 1)
d = [0] * (N + 1)
g = []
for _ in range(n):
    l, r = MII()
    if l > r:
        l, r = r, l
    d[l] += 1
    d[r + 1] -= 1 
    g.append((l, r, 0, 0)) 

for i in range(1, N):  # 包含A点的数量
    d[i] += d[i - 1]

res = [0] * (n + 1)
for i in range(1, q + 1):
    l, r = MII()
    res[i] = d[l]
    if l > r:
        l, r = r, l
    g.append((l, r, i, 1))
# 按端点排序是一个经典的做法，要多思考
g.sort(key=lambda x:(-x[1], x[0], x[3]))  # r由大到小排序。
for i in range(1, n + q + 1):
    l, r, idx, op = g[i - 1]
    if op == 0:
        tree.update(l, 1)  # 插入l
    else:
        res[idx] -= tree.query(l)  # l比当前的小，r又是有序的。说明当前区间被包含了

for i in range(1, q + 1):
    print(res[i])


