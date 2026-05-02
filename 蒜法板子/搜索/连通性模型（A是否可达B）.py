"""
dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
inf = float('inf')
sys.setrecursionlimit(114514)


def dfs(x, y):
    if x == xb and y == yb:
        return True
    s.add((x, y))
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < n and (a, b) not in s and g[a][b] != '#':
            if dfs(a, b):
                return True
    return False


t = II()
s = set()
for _ in range(t):
    s.clear()
    n = II()
    g = [I() for _ in range(n)]
    xa, ya, xb, yb = MII()
    if dfs(xa, ya):
        print("YES")
    else:
        print("NO")
"""