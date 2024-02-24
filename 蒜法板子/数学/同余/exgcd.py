

# https://www.acwing.com/solution/content/1393/  这篇题解帮助理解证明
# 裴蜀定理：对于任意的整数a,b,存在整数x,y使得ax+by=gcd(a,b)
# 解决水壶问题 https://leetcode.cn/problems/water-and-jug-problem/description/
def exgcd(a, b, x, y):
    if b == 0:   # b=0时, ax + by = a, 因此x=1, y=0
        return a, 1, 0
    d, y, x = exgcd(b, a % b, y, x)
    y -= a // b * x
    return d, x, y

def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0
    