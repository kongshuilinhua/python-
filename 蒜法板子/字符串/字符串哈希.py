# h[i]前i个字符的hash值
# 字符串变成一个p进制数字，体现了字符+顺序，需要确保不同的字符串对应不同的数字
# P = 131 Q = 32或  13331 Q=2^64，在99%的情况下不会出现冲突
# 使用场景： 两个字符串的子串是否相同

"""

n, m = MII()
s = ' ' + I()
P, Q = 131, 1 << 32
N = 100010
h, p = [0] * N, [1] * N
for i in range(1, n + 1):
    p[i] = p[i - 1] * P % Q  
    h[i] = (h[i - 1] * P + ord(s[i])) % Q  # 字符串前缀和

# 区间和公式的理解: ABCDE 与 ABC 的前三个字符值是一样，只差两位，
# 乘上P的二次方把 ABC 变为 ABC00, 再用 ABCDE - ABC00 得到 DE 的哈希值。
def query(l, r):
    return (h[r] - h[l - 1] * p[r - l + 1]) % Q

for _ in range(m):
    l1, r1, l2, r2 = MII()
    if query(l1, r1) == query(l2, r2):
        print("Yes")
    else:
        print("No")
        
"""

import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)
HBASE2 = random.randrange(HMOD)


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1, base2=HBASE2):
        self.mod, self.base1, self.base2 = mod, base1, base2
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        s_hash, s_pow = f_hash[:], f_pow[:]
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + ord(s[i])) % mod
            s_hash[i + 1] = (base2 * s_hash[i] + ord(s[i])) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
            s_pow[i + 1] = base2 * s_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow
        self.s_hash, self.s_pow = s_hash, s_pow

    def hashed(self, start, stop):
        return (
            (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start]) % self.mod,
            (self.s_hash[stop] - self.s_pow[stop - start] * self.s_hash[start]) % self.mod,
        )

    def get_hashes(self, length):
        return (
            [(self.f_hash[i + length] - self.f_pow[length] * self.f_hash[i]) % self.mod for i in range(self._len - length + 1)],
            [(self.s_hash[i + length] - self.s_pow[length] * self.s_hash[i]) % self.mod for i in range(self._len - length + 1)],
        )