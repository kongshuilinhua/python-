# 理论基础https://oi-wiki.org/math/number-theory/sqrt-decomposition/  
# 求解https://www.acwing.com/problem/content/4665/
# https://ac.nowcoder.com/acm/contest/96366/G
# 记 f(x)为x的所有因数（约数）的平方的和。f(4) = 1^2 + 2^2 + 4^2
# 求 f(1) + f(2) + ... + f(n) 的值
mod = int(1e9 + 7)
calc = lambda x: x * (x + 1) * (2 * x + 1) // 6 % mod
def solve():
    n = int(input())
    i = 1
    res = 0
    while i <= n:
        x = n // i       # 块内相同的值的个数
        y = n // x       # 块内的值，也就是当前块的右边界
        res += (calc(y) - calc(i - 1)) * x  # 当前块的左边界就是上一个的右边界       # 连续块的值 * 块的个数
        res %= mod
        i = y + 1
    print(res)
    return