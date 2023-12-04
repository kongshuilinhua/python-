'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-11 00:16:27
LastEditors: ElysiaRealme
Language: Python
'''
N = int(1e6 + 10)
is_prime = [True] * N  # 2, 3, 5, 7  质数个数数量级大概是n /（2 * lgn）
# O(nlog(logn))
def prime(n):
    for i in range(2, n + 1):
        if is_prime[i]:     # 质数的倍数一定是合数，都筛了。
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False

# O(n)
def find_prime(n):
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
        j = 0
         # 循环不变式：pi一定是pi*x的最小质因数     t=pi*x x是t的最大因数，则pi一定不大于x的最小质因数
        while i * prime[j] <= n:
            is_prime[i * prime[j]] = False
            if i % prime[j] == 0:  # 不是最小质因数了，退出，防止重复筛
                break
            j += 1
    return len(prime)
