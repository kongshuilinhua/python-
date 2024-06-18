# 用来求单个数据很大的组合数1<=b<=a<=1e18 1<=p<=1e5
"""

def C(n, m, p):
    if m < 0 or n < m:
        return 0
    if m == 0:
        return 1
    m = min(m, n - m)
    a = 1
    b = 1
    for i in range(1, m + 1):
        a = a * (n - i + 1) % p
        b = (b * i) % p
    return a * pow(b, p - 2, p) % p
 
def lucas(n, m, p):
    return C(n % p, m % p, p) * lucas(n // p, m // p, p) % p if m else 1

"""