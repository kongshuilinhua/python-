"""
某人从图中的左上角 A 出发，可以向下行走，也可以向右行走，直到到达右下角的 B 点。
在走过的路上，他可以取走方格中的数（取走后的方格中将变为数字0）。
此人从 A 点到 B 点共走了两次，试找出两条这样的路径，使得取得的数字和为最大。
"""
# https://codeforces.com/problemset/problem/213/C
# https://www.luogu.com.cn/problem/P7074

# 枚举横纵坐标值之和k，再枚举两人的横坐标
def func(n, g):
    f = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2 * n + 2)]
    for k in range(2, 2 * n + 1):
        for i1 in range(1, n + 1):
            for i2 in range(1, n + 1):
                j1 = k - i1
                j2 = k - i2
                if 1 <= j1 <= n and 1 <= j2 <= n:   # 判断越界
                    w = g[i1][j1]
                    if i1 != i2:             # 不重合
                        w += g[i2][j2]
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2 - 1] + w)  # 只看横坐标，就知道从上还是左移过来的了，2 * 2种情况
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2] + w)
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2 - 1] + w)
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2] + w)
    print(f[n * 2][n][n])

inf = float("inf")
def solve(n, g):
    f = [[-inf] * (n + 1) for _ in range(n + 1)]
    f[1][1] = 0
    for k in range(2, 2 * n + 1):
        for i1 in range(n, 0, -1):
            for i2 in range(n, 0, -1):
                j1 = k - i1
                j2 = k - i2
                if 0 < j1 <= n and 0 < j2 <= n:
                    w = g[i1][j1]
                    if i1 != i2:
                        w += g[i2][j2]
                    f[i1][i2] = max(f[i1 - 1][i2 - 1], f[i1 - 1][i2], f[i1][i2 - 1], f[i1][i2]) + w
    print(f[n][n])