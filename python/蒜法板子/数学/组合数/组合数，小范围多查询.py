N = 2020
mod = int(1e9 + 7)
f = [[0] * N for _ in range(N)]
for i in range(N):
    f[i][0] = 1
for i in range(N):
    for j in range(1, i + 1):
        f[i][j] = (f[i - 1][j] + f[i - 1][j - 1]) % mod