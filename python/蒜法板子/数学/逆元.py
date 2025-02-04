# 乘法逆元：a/b = a * x (mod m)  x为b的模m乘法逆元  即x = b^(-1)
# b存在乘法逆元的充要条件是 b与模数 m互质。当模数 m为质数时，b^(m-2)即为 b的乘法逆元。

"""
n = int(input())
for _ in range(n):
    a, p = map(int, input().split())
    print(pow(a, p - 2, p) if a % p else "impossible")

"""