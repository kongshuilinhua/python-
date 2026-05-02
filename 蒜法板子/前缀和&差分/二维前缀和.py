n, m, q = map(int, input().split())
N = 1010
a = [[0]]
s = [[0] * N for _ in range(N)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] + a[i][j] - s[i - 1][j - 1]
for _ in range(q):
    x1, y1, x2, y2 = list(map(int,input().split()))
    print(s[x2][y2] + s[x1 - 1][y1 - 1] - s[x1 - 1][y2] - s[x2][y1 - 1])  # (x1, y1) (x2, y2) 的所有元素


# 下标从0开始的做法
"""
s = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + (pizza[i][j] == 'A')
def query(x1, y1, x2, y2):
    print(s[x2][y2] + s[x1 - 1][y1 - 1] - s[x1 - 1][y2] - s[x2][y1 - 1])   # 这里和上面一样
"""

# 超大的子矩阵 https://atcoder.jp/contests/abc331/tasks/abc331_d

"""
n, q = MII()
g = [I() for _ in range(n)]
a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = 1 if g[i][j] == 'B' else 0
g.clear()
s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + a[i][j]


def calc(r, c):
    r += 1
    c += 1
    nr, r = divmod(r, n)
    nc, c = divmod(c, n)
    return s[n][n] * nr * nc + nr * s[n][c] + nc * s[r][n] + s[r][c]

def query(x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    return calc(x2, y2) - calc(x2, y1) - calc(x1, y2) + calc(x1, y1)

for _ in range(q):
    x1, y1, x2, y2 = MII()
    res = query(x1, y1, x2, y2)
    print(res)

"""