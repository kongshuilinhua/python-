'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
# 分组背包就是每组物品有若干个，同一组内的物品最多只能选一个。
def f(s, v, w):
    n, m = 0, 0  # n组物品， 容量为m
    N = 110
    f = [[0] * N for _ in range(N)], [0] * N
    for i in range(1, n + 1):  # 枚举组
        for j in range(m + 1):  # 枚举容量
            f[i][j] = f[i - 1][j]  # 不选
            for k in range(s[i]):  # 枚举组内用品
                if j >= v[i][k]:
                    f[i][j] = max(f[i][j], f[i - 1][j - v[i][k]] + w[i][k])
    return f[n][m]

# 滚动优化
"""
for i in range(n):
    for j in range(m, -1, -1):
        for k in range(s[i]):
            if j >= v[i][k]:
                f[j] = max(f[j], f[j - v[i][k]] + w[i][k])
"""
