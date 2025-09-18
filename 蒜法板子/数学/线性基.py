#https://leetcode.cn/problems/partition-array-for-maximum-xor-and-and/description/
#https://acm.hdu.edu.cn/showproblem.php?pid=3949
#https://www.luogu.com.cn/problem/P3857
#https://www.luogu.com.cn/problem/P3812
from typing import List


class LinearBasis:
    MAXB = 60
    def __init__(self, v: List[int]):
        self.a = v.copy()
        self.n = len(v)
        self.k = 0  # k为基的数量，不同异或和数为2^k(包含0)

    def build(self):
        for i in range(self.MAXB, -1, -1):
            p = -1
            for j in range(self.k, self.n):
                if (self.a[j] >> i) & 1:
                    p = j
                    break
            if p == -1:
                continue
            self.a[self.k], self.a[p] = self.a[p], self.a[self.k]
            for j in range(self.n):
                if j != self.k and ((self.a[j] >> i) & 1):
                    self.a[j] ^= self.a[self.k]
            self.k += 1
            if self.k == self.n:
                break

    # 子集最大异或和
    def max_xor(self) -> int:
        res = 0
        for x in self.a:
            res ^= x
        return res

    # 第k小异或和（不同的数字为2^k(包含0)，每个数字出现2^(n-k), 0出现2^(n-k)-1次）
    def kth_xor(self, x: int) -> int:
        # 可以构造出0
        if self.k < self.n:
            x -= 1
        if x >= (1 << self.k):
            return -1
        res = 0
        for i in range(self.k):
            if (x >> i) & 1:
                res ^= self.a[self.k - i - 1]
        return res
    def rank(self, v: int, empty: bool = True) -> int:
        """
        返回 v 在所有不同异或和按从小到大排序中的 0-based rank。
        返回 -1 表示 v 无法由（对应集合的）子集异或得到。
        """
        t = v
        idx = 0
        for t in range(self.k):  # a[t] 主元从高到低
            hb = self.a[t].bit_length() - 1
            if (v >> hb) & 1:
                v ^= self.a[t]
                idx |= 1 << (self.k - 1 - t)
        if v != 0:
            return inf
        if not empty and t == 0 and self.k == self.n:
            # 0 只由空集得到，将其视为不可达（非空子集）
            return inf
        return idx

