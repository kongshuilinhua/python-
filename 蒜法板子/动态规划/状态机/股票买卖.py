"""
给定一个长度为 N的数组，数组中的第 i个数字表示一个给定股票在第 i天的价格。
设计一个算法来计算你所能获取的最大利润，你最多可以完成 k笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。一次买入卖出合为一笔交易。
"""

# 朴素三维, 可能会MLE
"""
n, m = MII()
a = [0] + LII()
f = [[[-inf] * 2 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(n + 1):f[i][0][0] = 0
for i in range(1, n + 1):
    for j in range(m + 1):
        f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1] + a[i])
        f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - a[i])
res = 0
for i in range(m + 1):
    res = max(f[n][i][0], res)
print(res)
"""

# 滚动优化
"""
n, m = MII()
a = [0] + LII()
f = [[-inf] * 2 for _ in range(m + 2)]
f[0][0] = 0
for i in range(1, n + 1):
    for j in range(m, 0, -1):
        f[j][0] = max(f[j][0], f[j][1] + a[i])
        f[j][1] = max(f[j][1], f[j - 1][0] - a[i])
res = 0
for i in range(m + 1):
    res = max(f[i][0], res)
print(res)
"""