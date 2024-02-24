'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-16 08:00:54
LastEditors: ElysiaRealme
Language: Python
'''
from typing import *

# 求出模式串 P在字符串 S中所有出现的位置的起始下标。O(n+m)
def kmp(p: str, s: str):    # p是模式串， s是模板串（在s中找p）
    n, m = len(p), len(s)  # 下面已经+1，这句写在前面
    p, s = ' ' + p, ' ' + s
    N = 100010
    ne = [0] * N    # next数组
    j = 0
    for i in range(2, n + 1):
        while j and p[i] != p[j + 1]: 
            j = ne[j]
        j += p[i] == p[j + 1]  # 前后缀匹配成功， 长度+1
        ne[i] = j  # 记录
    j = 0
    for i in range(1, m + 1):
        while j and s[i] != p[j + 1]:
            j = ne[j]
        j += s[i] == p[j + 1]
        if j == n:
            print(i - j, end=' ')   # 打印匹配成功的起始下标
            j = ne[j]