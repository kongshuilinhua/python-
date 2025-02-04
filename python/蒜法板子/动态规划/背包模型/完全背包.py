# 和01背包不同的是每件物品有无限件可重复选
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

# 朴素做法是O(n^3)的，需要枚举个数K。我懒得写了，直接优化掉
def f(n, m):
    v, w = [0] * (n + 2), [0] * (n + 2)
    for i in range(1, n + 1):  # 为了方便写，下标是从1开始的
        v[i], w[i] = map(int, input().split())
    f = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = f[i - 1][j]
            if j >= v[i]:  # 因为可以重复选，所以是选f[i][j - v[i]] + w[i],这是和二维01背包唯一的不同
                f[i][j] = max(f[i - 1][j], f[i][j - v[i]] + w[i])
    return f[n][m]


# 滚动优化到一维
# 只需要正序即可，01逆序是为了防止重复选，而完全背包是可以的
"""
f = [0] * (m + 2)
for i in range(1, n + 1):    # 正着着枚举                
    for j in range(v[i], m + 1):
        f[j] = max(f[j], f[j - v[i]] + w[i])
print(f[m])
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

@lru_cache(None)
def dfs(i, c):
    if i < 0:
        return 0 if c >= 0 else -float('inf')
    if v[i] <= c:  # 可选
        return max(dfs(i - 1, c), dfs(i, c - v[i]) + w[i])  # 和01不同的地方，dfs(i, c - v[i]) + w[i]) 选了之后还可以选
    return dfs(i - 1, c)  # 不可选


print(dfs(n, m))


