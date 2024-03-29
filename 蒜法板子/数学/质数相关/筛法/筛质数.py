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
    # 从小到大枚举每个数，当前数字没被划掉，就是质数
    for i in range(2, n + 1):
        if is_prime[i]:   # 如果当前
            prime.append(i)
        j = 0
        while i * prime[j] <= n:      # 未越界，划掉
            is_prime[i * prime[j]] = False
            # 若i是质数，最多枚举到自身中断
            # 若i是合数，最多枚举到i的最小质因数中断
            if i % prime[j] == 0:  # 不是最小质因数了，退出，防止重复筛
                break
            j += 1
    return prime
