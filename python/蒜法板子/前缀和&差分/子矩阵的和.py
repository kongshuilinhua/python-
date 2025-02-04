"""
n, m, q = MII()
a = [LII() for _ in range(n)]
s = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + a[i][j]
for _ in range(q):
    x1, y1, x2, y2 = MII()
    print(s[x2][y2] + s[x1 - 1][y1 - 1] - s[x1 - 1][y2] - s[x2][y1 - 1])
    
"""