# https://zhuanlan.zhihu.com/p/131536831

# a ^ b === a ^ (b mod phi(m) + phi(m)) (mod m)  b >= phi(m)
def euler_phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

mod = 998244353
def solve(n):
    t = pow(2, n - 1, euler_phi(mod)) + euler_phi(mod) - n
    print(pow(2, t, mod) % mod)
    return
