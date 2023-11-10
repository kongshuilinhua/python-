'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-11-05 02:01:52
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

class TreeNode():
    def __init__(self):
        self.l = 0
        self.r = 0
        self.cnt = 0
        self.length = 0

def build(u, l, r):
    tr[u].l = l
    tr[u].r = r
    if l == r:
        return
    mid = (l + r) // 2
    build(u * 2, l, mid)
    build(u * 2 + 1, mid + 1, r)

def pushup(u):
    if tr[u].cnt:
        l, r = tr[u].l, tr[u].r
        tr[u].length = s[r + 1] - s[l]  # 向右偏移一位
    elif tr[u].l != tr[u].r:
        tr[u].length = tr[u * 2].length + tr[u * 2 + 1].length  # 左右儿子更新
    else:
        tr[u].length = 0

def modify(u, l, r, v):
    if tr[u].l >= l and tr[u].r <= r:  # 包含
        tr[u].cnt += v
    else:
        mid = (tr[u].l + tr[u].r) // 2
        if l <= mid:
            modify(u * 2, l, r, v)
        if r > mid:
            modify(u * 2 + 1, l, r, v)
    pushup(u)  # 更新

T = 1
while T:
    n = II()
    if not n:
        break
    edges = []
    s = set()
    for _ in range(n):
        x1, y1, x2, y2 = list(map(float, input().split()))
        s.add(y1)
        s.add(y2)
        edges.append((x1, y1, y2, 1))
        edges.append((x2, y1, y2, -1))
    s = sorted(s)  # 离散化y坐标
    edges.sort()  # 按x坐标排序
    m = len(s)
    mp = {x: i for i, x in enumerate(s)}
    tr = [TreeNode() for _ in range(m * 4)]
    build(1, 0, m)
    x1 = res = 0
    for x2, y1, y2, c in edges:
        res += tr[1].length * (x2 - x1)
        modify(1, mp[y1], mp[y2] - 1, c)  # 向左偏移一个
        x1 = x2
    print('Test case #%d' %T)
    print('Total explored area: %.2f' %res) 
    print()
    T += 1

