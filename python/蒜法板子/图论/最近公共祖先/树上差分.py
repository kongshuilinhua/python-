# https://ac.nowcoder.com/acm/contest/61132/I
"""
# 边差分
def solve():
    n, m, qrs = MII()
    g = [[] for _ in range(n)]
    edges = []
    for _ in range(n - 1):
        u, v, w = GMI()
        g[u].append((v, w + 1))
        g[v].append((u, w + 1))
        edges.append((u, v, w + 1))
    LCA = TreeAncestor(g)
    d = [0] * n

    for _ in range(m):
        x, y, w = GMI()
        w += 1
        d[x] += w
        d[y] += w
        d[LCA.get_lca(x, y)] -= 2 * w
    # 还原差分
    for x, y, w in edges:
        if LCA.depth[x] > LCA.depth[y]:
            x, y = y, x
        d[x] -= w   
        d[y] += w

    vals = [0] * n
    # 获得每条结点的权重，从叶子节点开始
    @bootstrap
    def dfs(x, fa):
        vals[x] = d[x]
        for y, w in g[x]:
            if y == fa:
                continue
            yield dfs(y, x)
            vals[x] += vals[y]
        yield
    dfs(0, -1)

    # 求根节点到每个节点的权重和
    q = deque([(0, -1)])
    while q:
        x, fa = q.popleft()
        for y, w in g[x]:
            if y == fa:
                continue
            vals[y] += vals[x]
            q.append((y, x))

    for _ in range(qrs):
        x, y = GMI()
        print(vals[x] + vals[y] - 2 * vals[LCA.get_lca(x, y)])

    return

"""