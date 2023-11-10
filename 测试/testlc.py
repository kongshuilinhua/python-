'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-30 20:00:36
LastEditors: ElysiaRealme
Language: Python
'''
"""
给你一个下标从 0 开始的整数数组 nums 。
nums 一个长度为 k 的 子序列 指的是选出 k 个 下标 i0 < i1 < ... < ik-1 ，如果这个子序列满足以下条件，我们说它是 平衡的 :
对于范围 [1, k - 1] 内的所有 j ,nums[ij] - nums[ij-1] >= ij - ij-1 都成立。
nums 长度为 1 的 子序列 是平衡的。
请你返回一个整数，表示 nums 平衡 子序列里面的 最大元素和 。
一个数组的 子序列 指的是从原数组中删除一些元素（也可能一个元素也不删除）后，剩余元素保持相对顺序得到的 非空 新数组。
"""
from typing import List


from bisect import *


class BIT:
    def __init__(self, n):
        self.tree = [0] * n  # 注意下标从1开始

    def lowbit(self, x):
        return x & (-x)

    # arr[i] += val
    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += self.lowbit(i)

    # 返回arr[:i+1]的sum
    def query(self, i):
        res = 0
        while i > 0:
            res = max(self.tree[i], res)
            i -= self.lowbit(i)
        return res


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        inf = float('inf')
        a = sorted(set([x - i for i, x in enumerate(nums)]))
        d = {x: i + 1 for i, x in enumerate(a)}
        tree = BIT(len(a) + 10)
        f = [0] * n
        for i, x in enumerate(nums):
            v = d[x - i]
            f[i] = x + tree.query(v)
            tree.update(v, f[i])
        return max(f)

# 使用方法
# edges 是边的列表，values 是节点的值的列表
# 函数返回可以获得的最大分数
s = Solution()
a = list(map(int, input().split()))
print(s.maxBalancedSubsequenceSum(a))


