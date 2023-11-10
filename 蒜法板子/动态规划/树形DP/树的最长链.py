'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-19 00:15:35
LastEditors: ElysiaRealme
Language: Python
'''

"""
n = II()
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = MII()
    g[a].append((b, c))
    g[b].append((a, c))

f1 = [0] * (n + 1)  # 最长路
f2 = [0] * (n + 1)  # 次长路
res = 0

def dfs(x, fa):
    global res
    for y, w in g[x]:
        if y != fa:
            dfs(y, x)
            if f1[y] + w >= f1[x]:  # 等于的情况是最长和次长链长度相同
                f2[x] = f1[x]
                f1[x] = f1[y] + w
            elif f1[y] + w > f2[x]:
                f2[x] = f1[y] + w
    res = max(res, f1[x] + f2[x])

dfs(1, 0)
print(res)

"""