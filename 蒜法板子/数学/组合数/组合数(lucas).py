# 用来求单个数据很大的组合数1<=b<=a<=1e18 1<=p<=1e5
"""
def C(a, b, p):
    res = 1
    j = a
    for i in range(1, b + 1):
        res = res * j % p
        res = res * pow(i, p - 2, p) % p
        j -= 1
    return res

def lucas(a, b, p):
    if a < p and b < p:
        return C(a, b, p)
    return C(a % p, b % p, p) * lucas(a // p, b // p, p) % p

"""