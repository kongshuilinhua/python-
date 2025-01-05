# 数字范围按位与[l, r]
def rangeBitwiseAnd(left: int, right: int) -> int:
    while left < right:
        right &= (right - 1)
    return right

# 2411. 按位或最大的最小子数组长度
# https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/description/
from typing import List
def smallestSubarrays(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    ors = []
    for i in range(n - 1, -1, -1):
        x = nums[i]
        ors.append([0, i])   # 按位或的值 + 对应子数组的右端点的最小值
        k = 0
        for p in ors:
            p[0] |= x
            if ors[k][0] == p[0]:
                ors[k][1] = p[1]  # 合并相同值，下标取最小的（因为值相同，而右边下标小）
            else:
                k += 1
                ors[k] = p    
        del ors[k + 1:]
        # ors的值是从左到右逐渐减小的，下标也是减小的
        # 本题只用到了 ors[0]，如果题目改成任意给定数值，可以在 ors 中查找
        res[i] = ors[0][1] - i + 1
    return res

# 1521. 找到最接近目标值的函数值
# https://leetcode.cn/problems/find-a-value-of-a-mysterious-function-closest-to-target/
def closestToTarget(arr: List[int], target: int) -> int:
    res = set()
    ors = set()
    for x in arr:
        ors = {y & x for y in ors}
        ors.add(x)
        res |= ors
    return min(abs(x - target) for x in res)

# 小美的区间异或和
# 1 1 0 1 1
#考虑每个pair(i , j)满足nums[i] ^ nums[j] = 1,包含(i , j)对的子数组数目有[0 - i] & [j , n - 1]一共 (i + 1) *(n - j)个，i的贡献就是 i + 1,枚举j，计算所有贡献就是了
# https://ac.nowcoder.com/acm/problem/259733

"""

def solve():
    n = II()
    a = LII()
    res = 0
    for i in range(32):
        cnt0 = cnt1 = 0
        for j in range(n):
            if a[j] >> i & 1:      # 当前位是1
                res += cnt0 * (n - j) * (1 << i)
                cnt1 += j + 1
            else:
                res += cnt1 * (n - j) * (1 << i)
                cnt0 += j + 1
            res %= mod
    print(res)

    return

"""
# https://www.marscode.cn/practice/ln2xx0pn0k5rd3?problem_id=7424418560667172908
# 149小K的区间与值和
"""
mod = int(1e9 + 7)
def solution(n: int, a: list) -> int:
    res = 0
    for i in range(32):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:      # 当前位是1
                res += cnt * (n - j) * (1 << i)
                res %= mod
                cnt += j + 1
    return res


if __name__ == '__main__':
    print(solution(4, [2, 3, 1, 2]) == 16)
    print(solution(3, [5, 6, 7]) == 25)
    print(solution(2, [1, 10]) == 0)
    print(solution(5, [1, 2, 4, 8, 16]) == 0)


"""


# 区间的异或和
"""
def get(n):
    d = [n, 1, n + 1, 0]
    return d[n % 4]
def solve():
    l, r = MII()
    print(get(r) ^ get(l - 1))
    return
"""

# 1~n 中第 k位上1 的个数,0<= n,0 <= k<= 30
def f(n, k):  
    return (n + 1) // (1 << k + 1) * (1 << k) + max((n + 1) % (1 << k + 1)- (1 << k), 0)

