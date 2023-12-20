"""
给定一棵树,树中包含n个结点编号1~n和n-1条无向边,每条边都有一个权值。
现在请你找到树中的一条最长路径。
换句话说，要找到一条路径，使得使得路径两端的点的距离最远。
"""

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