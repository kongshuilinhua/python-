'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-06 16:13:12
LastEditors: ElysiaRealme
Language: Python
'''
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

prime = find(n + 1)
for i in range(2, n + 1):
    if not is_prime[i]:
        continue
    res = 0
    j = i
    while j <= n:
        res += n // j
        j *= i
    print(i, res)

