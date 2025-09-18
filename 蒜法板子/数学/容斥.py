# https://leetcode.cn/problems/sum-of-beautiful-subsequences/
# https://codeforces.com/problemset/problem/803/F
from typing import *
N = int(7e4 + 10)
div = [[] for _ in range(N)]
for i in range(1, N):
    for j in range(i, N, i):
        div[j].append(i)
mod = int(1e9 + 7)
class BIT:
    def __init__(self, n):
        self.tree = [0] * n  # 注意下标从1开始

    def lowbit(self, x):
        return x & (-x)

    # arr[i] += val
    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += self.lowbit(i)

    # 返回arr[:i]的sum
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res
class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)
        g = [[] for _ in range(m + 1)]
        for x in nums:
            for d in div[x]:
                g[d].append(x)
        def calc(a, g):
            res = 0
            tree = BIT(m // g + 1)
            for x in a:
                x //= g
                cnt = tree.query(x - 1) + 1
                res += cnt
                tree.update(x, cnt)
            return res
        f = [0] * (m + 1)
        res = 0
        # f[i]为gcd为i的倍数的子序列个数
        # 倒序枚举i，减去i的倍数（大于i）的贡献
        for i in range(m, 0, -1):
            f[i] = calc(g[i], i)
            for j in range(2 * i, m + 1, i):
                f[i] -= f[j]
            res += f[i] * i
        return res % mod