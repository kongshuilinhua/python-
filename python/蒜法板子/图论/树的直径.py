"""
n = II()
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = MII()
    g[u].append((v, w))
    g[v].append((u, w))
res = 0
def dfs(x, fa):
    nonlocal res
    x_len = 0
    for y, w in g[x]:
        if y == fa:continue
        y_len = dfs(y, x) + w
        res = max(res, x_len + y_len)
        x_len = max(x_len, y_len)
    return x_len
dfs(1, 0)
print(res)
"""