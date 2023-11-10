import math
N = 200010
M = 18
f = [[0] * M for _ in range(N)]
n, m =  MII()
a = LII()

for i in range(n):
    f[i][0] = a[i]

def st():  # f[i,j]为以第i个数为起点，长度为2^j的一段区间中的最大值
    for j in range(1, M + 1):
        i = 0
        while i + (1 << j) <= n:   # i - > i+2^j - 1  = 两段 i -> i + 2^(j-1)和i+2^(j-1) - > i+2^j - 1
            f[i][j] = max(f[i][j - 1], f[i + (1 << j - 1)][j - 1])
            i += 1

def query(l, r):
    k = int(math.log2(r - l + 1))  # 2 ^ k <= length
    res = max(f[l - 1][k], f[r - (1 << k)][k])  # 可能重叠的两段，下标是1开始的，一段依附l，一段依附r
    return res

st()
for _ in range(m):
    l, r = MII()
    print(query(l, r))