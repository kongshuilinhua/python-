import sys
import os

# import time
from bisect import bisect_left, bisect_right
# import functools
from math import ceil, floor, gcd, factorial, sqrt, log2, log
import random
# import re
from collections import Counter, defaultdict, deque
# from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import accumulate, combinations, permutations
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase
from typing import *

input = lambda: sys.stdin.readline().rstrip("\r\n")

# --------------------
# 手写栈模板
# 克服py栈太浅的问题
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc
# --------------------


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

# sys.setrecursionlimit(int(1e5 + 10))根据需要调整递归深度
dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
inf = float('inf')
# RANDOM = random.randint(int(1e9 + 7), int(2e9 + 7)) # 防止卡哈希
mod = int(1e9 + 7)
# mod = 998244353

def solve():


    return


if __name__ == '__main__':
    # 1多组数据，0单组数据
    t = 1     
    if t:
        t = II()
        for _ in range(t):
            solve()
    else:
        solve()
