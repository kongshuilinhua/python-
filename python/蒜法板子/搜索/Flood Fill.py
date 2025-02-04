# 实际上就是求连通块的数量
# 典型题是AcWing1233全球变暖和1097池塘计数
from collections import deque


# n = len(g), m = len(g[0])
def FloodFill(g, n, m):
    dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
    s = set()

    def bfs(x, y):  # BFS 写法
        q = deque([(x, y)])
        s.add((x, y))
        while q:
            x, y = q.popleft()
            for i in range(8):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < n and 0 <= b < m and (a, b) not in s and g[a][b] == 'W':
                    q.append((a, b))
                    s.add((a, b))
        return 1

    res = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in s and g[i][j] == 'W':
                res += bfs(i, j)
    print(res)


"""
    def dfs(x, y):  # DFS写法
        s.add((x, y))
        for i in range(8):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < m and (a, b) not in s and g[a][b] == 'W':
                dfs(a, b)
"""
# 也可以在原地修改，提高效率
"""
def bfs(x, y):
    q = deque([(x, y)])
    g[x][y] = '.'
    while q:
        x, y = q.popleft()
        for i in range(8):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < m and g[a][b] == 'W':
                q.append((a, b))
                g[a][b] = '.'
    return 1
"""
