
def isBipartite(g):
    n = len(g)
    color = [0] * n  # 0表示未染色，1和2表示两种颜色
    def bfs(x, col):
        q = deque([(x, col)])
        while q:
            x, col = q.popleft()
            for y in g[x]:
                if not color[y]:  # 如果没染色
                    color[y] = 3 - col  # 染成另一种颜色
                    q.append((y, color[y]))
                elif color[y] == col:  # 相邻点的颜色和当前点相同
                    return False
        return True
    for i in range(n):
        if not color[i]:  # 未染色
            color[i] = 1
            if not bfs(i, 1):  # 染色失败，直接退出
                return False
    return True