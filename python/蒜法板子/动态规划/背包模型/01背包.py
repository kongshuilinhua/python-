'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
# 一共n件物品，背包容量为m。第 i件物品的体积是 vi，价值是 wi。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

def f(n, m):
    v, w = [0] * (n + 2), [0] * (n + 2)
    for i in range(1, n + 1):  # 为了方便写，下标是从1开始的
        v[i], w[i] = map(int, input().split())
    f = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = f[i - 1][j]
            if j >= v[i]:  # 装得下物品，装or不装取max
                f[i][j] = max(f[i - 1][j], f[i - 1][j - v[i]] + w[i])
    return f[n][m]


# 滚动优化到一维
# 逆序的原因：如果从小到达枚举，有可能更新f[7]的时候，f[4]已经选了这个物品，那么就相当于选了两次该物品，是错误的
# 逆序可以保证，更新f[7]的时候， f[4]还是未更新的状态。就是物品只能选一次
"""
f = [0] * (m + 2)
for i in range(1, n + 1):    # 倒着枚举                
    for j in range(m, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])
return f[m]
"""

from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10100)
N = 1010
v = [0] * N
w = [0] * N
n, m = map(int, input().split())
for i in range(n):
    v[i], w[i] = map(int, input().split())


# 另一种记忆化搜索的写法
# 记得调递归深度，防止爆栈
@lru_cache(None)
def dfs(i, c):
    if i < 0:
        return 0 if c >= 0 else -float('inf')
    if v[i] <= c:  # 可选
        return max(dfs(i - 1, c), dfs(i - 1, c - v[i]) + w[i])
    return dfs(i - 1, c)  # 不可选


print(dfs(n - 1, m))


# 二维01背包，直接再套一层
"""
for i in range(1, N + 1):
    for j in range(V, v[i] - 1, -1):
        for k in range(M, m[i] - 1, -1):
            f[j][k] = max(f[j][k], f[j - v[i]][k - m[i]] + w[i])
print(f[V][M])
"""