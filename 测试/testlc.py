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

class Solution:
    def placeWordInCrossword(self, g: List[List[str]], word: str) -> bool:
        n, m = len(g), len(g[0])
        k = len(word)
        def find1(x):
            a = []
            for i in range(n):
                st = -1
                j = 0
                while j < m:
                    if g[i][j] == x:
                        st = j
                        while j < m and g[i][j] == x:
                            j += 1
                        if (j - st + 1) >= k:
                            return True
                    else:
                        j += 1
            return False
        def find2(x):
            for row in zip(*g):
                st = -1
                j = 0
                while j < n:
                    if row[j] == x:
                        st = j
                        while j < n and row[j] == x:
                            j += 1
                        if (j - st + 1) >= k:
                            return True
                    else:
                        j += 1
            return False
        res1 = find1(word[0]) | find1(word[-1])
        res2 = find2(word[0]) | find2(word[-1])
        return res1 or res2

s = Solution()
g = [["#"," ","#"],[" "," ","#"],["#"," ","c"]]
word = "ca"
res = s.placeWordInCrossword(g, word)
print(res)
g = [["#"," ","#"],[" "," ","#"],["#","c"," "]]
word = "abc"
res = s.placeWordInCrossword(g, word)
print(res)
