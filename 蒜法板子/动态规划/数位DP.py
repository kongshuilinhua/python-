'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
# 数字计数通解，递归实现（需要记忆化搜索）
# python3的记忆化搜索比pypy3快！注意！！！

"""
LC2376. 统计特殊整数
如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。(数据：1e9)
"""
from functools import cache, lru_cache


def countSpecialNumbers(self, n: int) -> int:
    s = str(n)

    # i表示当前正在填哪位
    # mask表示已经填了的数字集合
    # is_limit表示前面所填数字是否是和n前面一一对应的，对应：当前最大int(s[i])，不对应:最大9
    # is_num表示前面是否填了数字，填了：可以从0开始，没填，可以跳过当前位置，或者从1开始
    # 注意：不允许出现前导零的情况！！！
    @cache  # 记忆化搜索
    def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
        if i == len(s):
            return int(is_num)  # is_num 为 True 表示得到了一个合法数字
        res = 0
        if not is_num:  # 可以跳过当前数位
            res = f(i + 1, mask, False, False)
        low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
        for d in range(low, up + 1):  # 枚举要填入的数字 d
            if (mask >> d & 1) == 0:  # d 不在 mask 中
                res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
        return res

    return f(0, 0, True, False)


# 求A ~ B之间0 ~ 9各有多少，确保（A < B）
s = ""


@lru_cache(None)
def f(i, cnt, is_limit, is_num):
    if i == len(s):
        return cnt
    res = 0
    if not is_num:
        res += f(i + 1, cnt, False, False)
    low = 0 if is_num else 1
    up = int(s[i]) if is_limit else 9
    for d in range(low, up + 1):
        res += f(i + 1, cnt + (d == now), is_limit and d == up, True)
    return res


def solve(n):
    global s
    s = str(n)
    f.cache_clear()   # 清除缓存
    return f(0, 0, True, False)  # 最后答案要取模


a, b = map(int, input().split())
if a > b: a, b = b, a
while a != 0 and b != 0:
    for i in range(10):
        now = i
        print(solve(b) - solve(a - 1), end=' ')  # 如果需要，一定要在这里取模！！！
    print()
    a, b = map(int, input().split())
    if a > b: a, b = b, a
