 
class Prime:
    def prime_sieve(self, n):
        """returns a sieve of primes >= 5 and < n"""
        flag = n % 6 == 2
        sieve = bytearray((n // 3 + flag >> 3) + 1)
        for i in range(1, int(n**0.5) // 3 + 1):
            if not (sieve[i >> 3] >> (i & 7)) & 1:
                k = (3 * i + 1) | 1
                for j in range(k * k // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
                for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
        return sieve
 
    def prime_list(self, n):
        """returns a list of primes <= n"""
        res = []
        if n > 1:
            res.append(2)
        if n > 2:
            res.append(3)
        if n > 4:
            sieve = self.prime_sieve(n + 1)
            res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
        return res
     
    def __init__(self, n) -> None:
        self.primes = self.prime_list(n)
     
    def dissolve(self, num):
        '''prime factor decomposition of num'''
        lst = []
        idx = -1
        for prime in self.primes:
            if prime * prime > num:
                break
 
            if num % prime == 0:
                lst.append([prime, 0])
                idx += 1
                 
            while num % prime == 0:
                lst[idx][1] += 1
                num //= prime
                 
        if num != 1:
            lst.append([num, 1])
             
        return lst
 
    def GetAllFactors(self, num, SORT = False):
        res = [1]
        if num == 1:
            return res
        else:
            for a, b in self.dissolve(num):
                mul = a
                k = len(res)
                for _ in range(b):
                    for i in range(k):
                        res.append(res[i] * mul)
                    mul *= a
             
            if SORT:
                res.sort()
             
            return res
     
    def primitive_root(self, num):
        '''
        check whether num is prime
        '''
        g = 1
        DIS = self.dissolve(num)
 
        while True:
            for a, b in DIS:
                if pow(g, (num - 1) // a, num) == 1:
                    break
            else:
                break
            g += 1
         
        return g
 



class PrimeTable:
    def __init__(self, n:int) -> None:
        self.n = n
        self.primes = []
        self.max_div = list(range(n+1))
        self.max_div[1] = 1
        self.phi = list(range(n+1))
 
        for i in range(2, n + 1):
            if self.max_div[i] == i:
                self.primes.append(i)
                for j in range(i, n+1, i):
                    self.max_div[j] = i
                    self.phi[j] = self.phi[j] // i * (i-1)
 
    def is_prime(self, x:int):
        if x < 2: return False
        if x <= self.n: return self.max_div[x] == x
        for p in self.primes:
            if p * p > x: break
            if x % p == 0: return False
        return True
 
    def prime_factorization(self, x:int):
        if x > self.n:
            for p in self.primes:
                if p * p > x: break
                if x <= self.n: break
                if x % p == 0:
                    cnt = 0
                    while x % p == 0: cnt += 1; x //= p
                    yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.max_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1
 
    def get_factors(self, x:int):
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors
    
