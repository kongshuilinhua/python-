'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-19 07:54:08
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

n = II()
g = [[] for _ in range(n)]
d1 = [0] * n
d2 = [0] * n
p1 = [0] * n
up = [0] * n # 向


for _ in range(n - 1):
    a, b, c = GMI()
    g[a].append((b, c + 1))
    g[b].append((a, c + 1))


def dfs(x, fa):
    for y, w in g[x]:
        if y != fa:
            d = dfs(y, x) + w
            if d >= d1[x]:
                d2[x] = d1[x]  # 更新最长和次长路径，并记录当前路径是从哪下去的
                d1[x] = d
                p1[x] = y
            elif d > d2[x]:
                d2[x] = d
    return d1[x]


dfs(0, -1)

def reroot(x, fa):
    for y, w in g[x]:
        if y != fa:
            if p1[x] == y:  # 如果x向下走的最大路径经过y的话,那么只能用次长距离
                up[y] = max(up[x], d2[x]) + w
            else:
                up[y] = max(up[x], d1[x]) + w  # 不经过的话用最长更新
            reroot(y, x)

reroot(0, -1)
res = d1[0]
for i in range(1, n):
    res = min(res, max(d1[i], up[i]))
print(res)