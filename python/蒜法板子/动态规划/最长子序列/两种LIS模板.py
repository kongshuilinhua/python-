'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
from bisect import bisect_left
from typing import List

# 题：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 扩展，限制的LIS，需要线段树来解决


# O(n2)的dp写法
def lengthOfLIS(nums: List[int]) -> int:
    f = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                f[i] = max(f[i], f[j] + 1)
    return max(f)


# 贪心 + 二分
def lengthOfLIS2(nums: List[int]) -> int:
    g = []
    for x in nums:
        j = bisect_left(g, x)
        if j == len(g):
            g.append(x)
        else:
            g[j] = x    # 尽量变小，可以让序列更长
    return len(g)
