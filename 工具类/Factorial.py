class Factorial:
    def __init__(self, N, mod) -> None:
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod
      
    def comb(self, n, m):
        if n < 0 or m < 0 or n < m:
            return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod
     
    def inv(self, n):
        assert n != 0
        return self.f[n - 1] * self.g[n] % self.mod
      
    def perm(self, n, m):
        if n < 0 or m < 0 or n < m:
            return 0
        return self.f[n] * self.g[n - m] % self.mod
  
    def catalan(self, n):
        #TODO: check 2 * n < N#
        return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod
     
    #N个不同的物品放进m个不同的集合，保证每个集合都不是空集#
    def sterling(self, n, m):
        if n < m:
            return 0
        else:
            res = 0
            for i in range(m + 1):
                t = self.comb(m, i) * pow(m - i, n, self.mod) % self.mod
                if i & 1:
                    res -= t
                else:
                    res += t
                res %= self.mod
            return res * self.g[m] % self.mod
