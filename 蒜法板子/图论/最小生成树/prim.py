'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-08 17:31:14
LastEditors: ElysiaRealme
Language: Python
'''
"""
inf = float('inf')

n, m = MII()
g = [[inf] * (n + 1) for _ in range(n + 1)]  # 注意初始化为inf
dis = [inf] * (n + 1)   # 各个结点到生成树的距离

# 思路是每次找已知点的邻边最小加入即可， 然后更新

def prim():
    res = 0
    dis[1] = 0
    s = set()
    for i in range(n):
        t = -1
        for j in range(1, n + 1):       # 如果没有在树中，且到树的距离最短，则选择该点
            if j not in s and (t == -1 or dis[t] > dis[j]):
                t = j
        if i and dis[t] == inf:
            return inf
        if i:
            res += dis[t]
        s.add(t)
        for j in range(1, n + 1):  # 更新生成树外的点到生成树的距离
            dis[j] = min(dis[j], g[t][j])
    return res


for _ in range(m):
    a, b, c = MII()
    g[a][b] = g[b][a] = min(g[a][b], c)

res = prim()
print("impossible" if res == inf else res)

"""