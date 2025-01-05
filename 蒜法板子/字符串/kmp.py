
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




# 求出next数组。O(n)
# s[:i]的最长真前后缀长度为pi[i]
def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi

# 返回字符串 s 中所有匹配模式串 pat 的起始下标
def match(s, pat):
    pi = partial(pat)

    g, idx = 0, []
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            idx.append(i + 1 - g)
            g = pi[g - 1]

    return idx

# 判断字符串 s 中是否包含模式串 pat
def string_find(s, pat):
    pi = partial(pat)

    g = 0
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            return True

    return False