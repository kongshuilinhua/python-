# https://ac.nowcoder.com/acm/contest/95118/D
"""
def solve():
    n = II()
    a = LII()
    res = n
    N = int(3e3 + 10)
    g = [[] for _ in range(N + 10)]
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            g[j].append(i)
    # 以x为结尾的公比为y的子序列个数
    f = [[0] * (N + 10) for _ in range(N + 10)]
    cnt = [0] * (N + 10) # x出现的次数
    for x in a:
        for y in g[x]:
            res += f[x // y][y] + cnt[x // y]
            f[x][y] += f[x // y][y] + cnt[x // y]
        cnt[x] += 1
    
    print(res % mod)
    return
"""