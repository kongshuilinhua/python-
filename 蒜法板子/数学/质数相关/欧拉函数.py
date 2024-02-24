# 定义：1~N中与N互质的数的个数，记为φ(N)。
# 在算数基本定理中，我们知道N可以分解为N=p1^a1*p2^a2*...*pk^ak，其中p1,p2,...,pk是N的所有质因数。
# (phi)φ(N) = N * ((p1 - 1) / p1) * ((p2 - 1) / p2) * ... * ((pk - 1) / pk)
# 模板 https://www.acwing.com/problem/content/875/
# 筛法求欧拉函数 https://www.acwing.com/problem/content/876/
# 应用：n很大的情况，https://www.acwing.com/problem/content/4971/
def solve():
    n = int(input())
    i = 2
    res = n
    while i * i <= n:
        if n % i == 0:
            res = res * (i - 1) // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res * (n - 1) // n
    print(res)

    return