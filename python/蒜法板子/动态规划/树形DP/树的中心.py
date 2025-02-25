"""
给定一棵树，树中包含 n个结点编号1~n和n-1条无向边,每条边都有一个权值。
请你在树中找到一个点，使得该点到树中其他结点的最远距离最近。
n = II()
g = [[] for _ in range(n)]
d1 = [0] * n
d2 = [0] * n
p1 = [0] * n
up = [0] * n # 向


for _ in range(n - 1):
    a, b, c = GMI()
    g[a].append((b, c + 1))
    g[b].append((a, c + 1))


def dfs(x, fa):
    for y, w in g[x]:
        if y != fa:
            d = dfs(y, x) + w
            if d >= d1[x]:
                d2[x] = d1[x]  # 更新最长和次长路径，并记录当前路径是从哪下去的
                d1[x] = d
                p1[x] = y
            elif d > d2[x]:
                d2[x] = d
    return d1[x]


dfs(0, -1)

def reroot(x, fa):
    for y, w in g[x]:
        if y != fa:
            if p1[x] == y:  # 如果x向下走的最大路径经过y的话,那么只能用次长距离
                up[y] = max(up[x], d2[x]) + w
            else:
                up[y] = max(up[x], d1[x]) + w  # 不经过的话用最长更新
            reroot(y, x)

reroot(0, -1)
res = d1[0]
for i in range(1, n):
    res = min(res, max(d1[i], up[i]))
print(res)
"""