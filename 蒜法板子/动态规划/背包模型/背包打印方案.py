"""
path = []  # 逆序打印path
def dfs(i, j):
    if i <= 0:
        return
    for k in range(j + 1):   # 逆序可以找到字典序最小的答案
        if f[i][j] == f[i - 1][j - k] + w[i][k]:
            path.append(k)
            dfs(i - 1, j - k)
            return

dfs(n, m)
"""

# 求最优解有多少个方案数
"""
mod = int(1e9 + 7)
n, m = MII()
f = [0] * (m + 2)
cnt = [1] * (m + 2)  # cnt[i]为背包容积为i时总价值为最佳的方案数,不取也是一种方案
for i in range(n):
    v, w = MII()
    for j in range(m, v - 1, -1):
        value = f[j - v] + w
        if f[j] < value:       # 取
            f[j] = value
            cnt[j] = cnt[j - v]
        elif value == f[j]:   # 取和不取都行
            cnt[j] = (cnt[j] + cnt[j - v]) % mod
print(cnt[m])
"""
# 字典序最小的方案
"""
n, m = MII()
v, w = [0] * (n + 2), [0] * (n + 2)
for i in range(1, n + 1):  # 为了方便写，下标是从1开始的
    v[i], w[i] = MII()
f = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(n, -1, -1):
    for j in range(m + 1):
        f[i][j] = f[i + 1][j]
        if j >= v[i]:  # 装得下物品，装or不装取max
            f[i][j] = max(f[i][j], f[i + 1][j - v[i]] + w[i])
j = m
for i in range(1, n + 1):  # 优先取小的
    if j >= v[i] and f[i][j] == f[i + 1][j - v[i]] + w[i]:
        print(i, end=' ')
        j -= v[i]
"""


# 完全背包的方案  #LChttps://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
"""
class Solution:
    def largestNumber(self, cost: List[int], m: int) -> str:
        f = [-inf] * (m + 1)
        f[0] = 0
        for i in range(9):
            for j in range(cost[i], m + 1):
                f[j] = max(f[j], f[j - cost[i]] + 1)
        if f[m] == -inf:
            return "0"
        res = []
        for i in range(8, -1, -1):
            v = cost[i]
            while m >= v and f[m] == f[m - v] + 1:
                res.append(i + 1)
                m -= v
        return "".join(map(str, res))
        
"""