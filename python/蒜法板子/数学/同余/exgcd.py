

# https://www.acwing.com/solution/content/1393/  这篇题解帮助理解证明
# 裴蜀定理：对于任意的整数a,b,存在整数x,y使得ax+by=gcd(a,b) 并且gcd(a, b)是ax+by的因子
# 推广ax+by=n*gcd(a,b)也成立
# 多个数字a1,a2,...,an的最大公约数gcd(a1,a2,...,an)也可以用扩展欧几里得算法求解

# 解决水壶问题 https://leetcode.cn/problems/water-and-jug-problem/description/
# https://www.luogu.com.cn/problem/P3951

# 进一步的结论, 若a，b互质 
# 记 C=ab-a-b。则有结论：对任意的整数 n，n 与 C-n 中有且仅有一个可以被表示。
#即：可表示的数与不可表示的数在区间 [0,C] 对称（关于 C 的一半对称）。0 可被表示，C 不可被表示；负数不可被表示，大于C的数都可被表示。
def exgcd(a, b, x, y):
    if b == 0:   # b=0时, ax + by = a, 因此x=1, y=0
        return a, 1, 0
    d, y, x = exgcd(b, a % b, y, x)
    y -= a // b * x
    return d, x, y

# 返回gcd(a, b)和x, y, 使得ax + by = gcd(a, b)
def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0
    