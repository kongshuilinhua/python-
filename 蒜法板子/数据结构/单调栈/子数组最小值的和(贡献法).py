# LC2104. 子数组范围和（单调栈的应用）
from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sumSubarrayMaxs(arr: List[int]) -> int:  # 计算每个数字作为最大值的贡献
            n = len(arr)
            left, right = [-1] * n, [n] * n
            st = []
            for i, x in enumerate(arr):
                while st and arr[st[-1]] <= x:  # 左边是大于   
                    st.pop()
                if st:
                    left[i] = st[-1]
                st.append(i)
            st = []
            for i in range(n - 1, -1, -1):
                while st and arr[st[-1]] < arr[i]:  # 右边是大于等于， 这样做是为了防止重复计算
                    st.pop()
                if st:
                    right[i] = st[-1]
                st.append(i)
            res = 0
            for i, x in enumerate(arr):
                res += x * (i - left[i]) * (right[i] - i)
            return res
        r1 = sumSubarrayMaxs(nums)
        nums = [-x for x in nums]  # 计算小技巧，数组取反就是最小值的贡献
        r2 = sumSubarrayMaxs(nums)
        return r1 + r2
    

# 或者把两次循坏改成一次循环
"""
注意到在计算 left的过程中,如果栈顶元素 ≥arr[i]，那么 i 就是栈顶元素的右边界，因此前两个循环可以合并。
更详细的解释：对于栈顶元素 t, 如果 t 右侧有多个小于或等于 t 的元素，那么 t 只会因为右侧第一个小于或等于 t 的元素而出栈，这恰好符合右边界的定义。
"""
def sumSubarrayMaxs(arr: List[int]) -> int:  # 计算每个数字作为最大值的贡献
    n = len(arr)
    left, right = [-1] * n, [n] * n
    st = []
    for i, x in enumerate(arr):
        while st and arr[st[-1]] <= x:  # 左边是大于   
            right[st.pop()] = i   # # i恰好是栈顶的右边界
        if st:
            left[i] = st[-1]
        st.append(i)
    res = 0
    for i, x in enumerate(arr):
        res += x * (i - left[i]) * (right[i] - i)
    return res