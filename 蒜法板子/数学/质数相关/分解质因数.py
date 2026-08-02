
N = int(1e6 + 10)

is_prime = [True] * N
minp = [0] * N   # minp[x] = x 的最小质因子


# O(n) 线性筛 + 预处理最小质因子
def find_prime(n):
    prime = []

    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            minp[i] = i

        j = 0
        while j < len(prime) and i * prime[j] <= n:
            is_prime[i * prime[j]] = False

            # i * prime[j] 的最小质因子就是 prime[j]
            minp[i * prime[j]] = prime[j]

            if i % prime[j] == 0:
                break

            j += 1

    return prime


ps = find_prime(N - 5)

def get_prime_factors(x):
    res = []
    while x > 1:
        p = minp[x]
        res.append(p)

        while x % p == 0:
            x //= p

    return res

# 根号n的时间复杂度
def div(x):
    res = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            s = 0
            while x % i == 0:
                x //= i
                s += 1
            res.append([i, s])
        i += 1
    if x > 1:                   # 最后可能还剩一个
        res.append([x, 1])
    return res

from collections import Counter
def div(x):
    res = Counter()
    i = 2
    while i * i <= x:
        if x % i == 0:
            s = 0
            while x % i == 0:
                x //= i
                s += 1
            res[i] += s
        i += 1
    if x > 1:                   # 最后可能还剩一个
        res[x] += 1
    return res