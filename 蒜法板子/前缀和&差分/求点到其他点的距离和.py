from itertools import accumulate
from typing import List


def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    n = len(nums)
    s = list(accumulate(nums))
    res = [0] * n          # res[i] = 前面的个数 * cur - 前面总和 + 后面的和 - 后面个数 * cur
    for i, x in enumerate(nums):
        res[i] = (i + 1) * x - s[i] + (s[n - 1] - s[i]) - (n - i - 1) * x
    return res
