
# 基本公式：n个物品选k个的   n! // (k!(n - k)!)
"""
N = int(1e5 + 10)
fac = [1] * N
infac = [1] * N
mod = int(1e9 + 7)
for i in range(1, N):
    fac[i] = fac[i - 1] * i % mod
    infac[i] = infac[i - 1] * pow(i, mod - 2, mod) % mod

for _ in range(n):
    a, b = MII()
    print(fac[a] * infac[a - b] % mod * infac[b] % mod)

"""