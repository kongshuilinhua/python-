# 每种物品有数量限制
def f():
    N = 1100
    n, m = map(int, input().split())
    v, w, s = [0] * N, [0] * N, [0] * N
    for i in range(1, n + 1):
        v[i], w[i], s[i] = map(int, input().split())
    f = [[0] * N for _ in range(N)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(s[i] + 1): # 枚举组内的数量
                if j < k * v[i]:
                    break
                f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i])
    return f[n][m]

# 滚动优化，和01背包是同样的思路，需要逆序
# 枚举方案数https://leetcode.cn/problems/number-of-ways-to-earn-points/description/
# 记得从物品1开始，否则就重复了
"""
## 复杂度n * m * s
for i in range(1, n + 1):
    for j in range(m, v[i] - 1, -1):
        for k in range(s[i] + 1):
            if j < k * v[i]:
                break
            f[j] = max(f[j], f[j - k * v[i]] + k * w[i])
            
"""

# 多重背包的二进制优化
# 思路是转成01背包，但是枚举数量的时候用二进制枚举，例如7，可以分解为1 2 4三次枚举得到，结果是相同的
"""

# 复杂度 n * m * logs
n, m = MII()
v, w = [0], [0]
f = [0] * (m + 1)
for _ in range(n):  # 每组拆分成二进制表示
    a, b, s = MII()
    k = 1
    while k <= s:
        v.append(a * k)  # 拆分的体积
        w.append(b * k)  # 差分的价值
        s -= k  
        k *= 2
    if s:
        v.append(a * s)  # 最后还剩余的部分
        w.append(b * s)
for i in range(1, len(v)):
    for j in range(m, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])
print(f[m])
"""



## 单调队列优化
"""
n, m = MII()

f = [0] * (m + 1)

for i in range(1, n + 1):
    v, w, s = MII()
    g = f.copy()
    for j in range(v):
        q = deque()
        for k in range(j, m + 1,  v):
            while q and k - q[0] > s * v:
                q.popleft()
            while q and g[q[-1]] + (k - q[-1]) // v * w <= g[k]:
                q.pop()
            q.append(k)
            f[k] = max(f[k], g[q[0]] + (k - q[0]) // v * w)
print(f[m])
"""