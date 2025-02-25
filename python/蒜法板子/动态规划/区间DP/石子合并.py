'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-16 20:06:43
LastEditors: ElysiaRealme
Language: Python
'''

"""
# 每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和，合并后与这两堆石子相邻的石子将和新堆相邻，合并时由于选择的# 顺序不同，合并的总代价也不相同。
n = II()
a = [0] + LII()
s = [0] * (n + 1)  # 下标从1开始
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
f = [[0] * (n + 1) for _ in range(n + 1)]
for length in range(2, n + 1): # 枚举合并的长度
    i = 1
    while i + length - 1 <= n: # 枚举左端点， 计算出右端点
        l, r = i, i + length - 1
        f[l][r] = inf
        for k in range(l, r):
            f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1])
        i += 1
        
print(f[1][n])


"""


# 环形

"""

n = II()
a = LII()
a = [0] + a + a
s = [0] * (n * 2 + 1)  # 下标从1开始
for i in range(1, n * 2 + 1):
    s[i] = s[i - 1] + a[i]

f = [[inf] * (n * 2 + 1) for _ in range(n * 2 + 1)]
g = [[-inf] * (n * 2 + 1) for _ in range(n * 2 + 1)]

for i in range(2 * n + 1):
    f[i][i] = g[i][i]=  0

for length in range(2, n + 1): # 枚举合并的长度
    i = 1
    while i + length - 1 <= 2 * n: # 枚举左端点， 计算出右端点
        l, r = i, i + length - 1
        for k in range(l, r):
            f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1])
            g[l][r] = max(g[l][r], g[l][k] + g[k + 1][r] + s[r] - s[l - 1])
        i += 1
        
mi = min(f[i][i + n - 1] for i in range(1, n + 1))
mx = max(g[i][i + n - 1] for i in range(1, n + 1))
print(mi)
print(mx)

"""