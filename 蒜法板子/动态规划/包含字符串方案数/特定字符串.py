# 包含三个shs的方案数 https://www.matiji.net/exam/brushquestion/17/4347/179CE77A7B772D15A8C00DD8198AAC74?from=1

"""
mod = int(1e9 + 7)
n = II()
pre = [[0] * 3 for _ in range(4)]
pre[0][0] = 1
f = [[0] * 3 for _ in range(4)]
res = 0
for i in range(1, n + 1):           # f[x] 表示凑好了x-1个shs
    for j in range(3):              # 0:末尾是完整shs和不是s   1:末尾单独是s      2:末尾单独是sh
        f[j][0] = (pre[j - 1][2] + pre[j][0] * 25 + pre[j][1] * 24 + pre[j][2] * 25) % mod
        f[j][1] = (pre[j][0] + pre[j][1]) % mod
        f[j][2] = pre[j][1] % mod
    res = (res * 26 + pre[2][2]) % mod
    for j in range(3):
        pre[j][0], pre[j][1], pre[j][2] = f[j][0], f[j][1], f[j][2]
print(res % mod)


"""

# 包含txt的方案数  https://ac.nowcoder.com/acm/contest/70845/C
"""
mod = 998244353
N = int(2e5 + 10)

res = [0] * N
pre = [0] * 3
pre[0] = 1
f = [0] * 3
for i in range(1, N):
    #0 others 1 t 2 tx
    f[0] = (pre[0] * 25 + pre[1] * 24 + pre[2] * 25) % mod
    f[1] = (pre[0] + pre[1]) % mod
    f[2] = pre[1] % mod
    res[i] = (pow(26, i, mod) - sum(f)) % mod
    pre = f[:]
t = II()
for _ in range(t):
    n = II()
    print(res[n])
"""

# 重排后包含可以用容斥原理做 https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/description/
