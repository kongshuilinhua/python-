"""
约数个数定理：
若n = p1^a1 * p2^a2 * ... * pk^ak, 则n的约数个数为(a1 + 1) * (a2 + 1) * ... * (ak + 1)
证明:pi^ai的约数有pi^0, pi^1, pi^2, ..., pi^ai, 一共ai + 1个
根据乘法原理, d(n) = (a1 + 1) * (a2 + 1) * ... * (ak + 1)
"""

N = int(1e6 + 10)
is_prime = [True] * N  # 2, 3, 5, 7  质数个数数量级大概是n /（2 * lgn）
a = [0] * N  # 记录i的最小质因子的次数  
d = [0] * N  # 记录i的约数个数

# O(n)
def find_prime(n):
    d[1] = 1
    prime = []
    for i in range(2, n + 1):
        # 若i是质数，质因数个数为1，约数个数为2
        if is_prime[i]:
            a[i] = 1
            d[i] = 2
            prime.append(i)
        j = 0
        # 每个合数m都是被最小质因数筛掉的
        # 设prime[j]是m的最小质因数， 则m被prime[j]*i筛掉
        while i * prime[j] <= n:
            m = i * prime[j]
            is_prime[m] = False
            # 若i被prime[j]整除，m的最小质因数一定是prime[j]
            if i % prime[j] == 0:  
                a[m] = a[i] + 1  # 最小质因数个数+1
                # d[i] = (a[i] + 1) * ... * (ak + 1)
                # d[m] = (a[m] + 1) * ... * (ak + 1)
                d[m] = d[i] // a[m] * (a[m] + 1)
                break
            else:
                # i不能被prime[j]整除,i不包含质因子prime[j]
                a[m] = 1
                d[m] = d[i] * 2
            j += 1
    


def solve(n):
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    res = sum(phi[1: n + 1])
    print(res)
            
        
        
