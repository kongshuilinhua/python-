# Acwing迷宫问题
# 输出从左上角到右下角的最短路线，如果答案不唯一，输出任意一条路径均可。
from collections import deque


def BFS(n, g):
    dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
    path = [[-1] * (n + 2) for _ in range(n + 2)]

    def bfs(x, y):
        q = deque([[x, y]])
        while q:
            x, y = q.popleft()
            for i in range(4):
                a, b = x + dx[i], y + dy[i]           # 注意这里0代表可以走的路径
                if 0 <= a < n and 0 <= b < n and path[a][b] == -1 and g[a][b] == 0:
                    q.append([a, b])
                    path[a][b] = (x, y)

    bfs(n - 1, n - 1)
    ed = (0, 0)
    while True:
        print(ed[0], ed[1])
        if ed == (n - 1, n - 1):
            break
        ed = path[ed[0]][ed[1]]
