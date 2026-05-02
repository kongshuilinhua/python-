# LC108双周赛

"""
给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个交替子序列：
m 大于 1 。
s1 = s0 + 1 。
下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。
子数组是一个数组中一段连续 非空 的元素序列。
"""
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        i, n = 0, len(nums)
        # 分组循环
        # 外层枚举子数组起点
        # 每层扩展子数组右端点
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            i0 = i # 记录起点
            i += 1 # 此时i的含义变成了子数组右端点
            while i < n and nums[i] == nums[i0 + (i - i0) % 2]: # 周期
                i += 1
            res =max(res, i - i0)
            i -= 1  # 本题需要回退
        return res

