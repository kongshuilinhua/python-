N = int(1e6 + 10)
is_prime = [True] * N

def find(n):
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
        j = 0
        while i * prime[j] <= n:
            is_prime[i * prime[j]] = False
            if i % prime[j] == 0:
                break
            j += 1
    return prime

n = int(input())

prime = find(n)  # 直接枚举
for i in prime:
    res = 0
    j = i
    while j <= n:  # 阶乘中i以及i的倍数的个数
        res += n // j
        j *= i
    print(i, res)
