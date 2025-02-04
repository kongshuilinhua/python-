
# 直接传入原数组,查询的时候不用给下标减一[1, n]
class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        # 从大到小扩展
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            # 判断是否能够扩展成功
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1

from bisect import *


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

    # 返回arr[:i+1]的sum
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res


# 附上求逆序对板子
n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
res = 0
tree = BIT(len(a) + 1)
for x in a:
    i = bisect_right(b, x)  # 比当前元素大的第一个元素，注意这个下标从0开始，而BIT是从1开始的
    res += tree.query(n) - tree.query(i)  # 相减得到比当前大的
    tree.update(i, 1)  # 将索引i处的树状数组值加1
print(res)


# 值域线段树求维护带修改的中位数(树上二分)
# https://ac.nowcoder.com/acm/contest/61132/L


"""

def solve():
    n, k = MII()
    a = LII()
    tree = FenwickTree([0] * (int(1e6) + 1))
    for i, x in enumerate(a):
        tree.update(x, 1)
    for _ in range(k):
        p, x = MII()
        p -= 1
        tree.update(a[p], -1)
        tree.update(x, 1)
        a[p] = x
        print(tree.findkth(n // 2))
"""

# 进阶版 https://codeforces.com/gym/104901/problem/K
"""
def solve():
    n, k = MII()
    a = LII()
    for i in range(1, n + 1):
        a[i - 1] -= i
    b = sorted(set(a))
    d = {x:i + 1 for i, x in enumerate(b)}
    b = [0] + b
    m = len(d)
    a = [d[x] for x in a]
    tr1 = [0] * (m + 1)
    tr2 = [0] * (m + 1)
    sum = 0
    def update(x, v):
        nonlocal sum
        sum += b[x] * v  # 当前的和
        i = x
        while i <= m:
            tr1[i] += v  # 个数
            tr2[i] += b[x] if v == 1 else -b[x]  # 前缀和
            i += i & -i

    def calc(len):
        k = len // 2 + 1
        idx = ans1 = ans2 = 0
        for i in reversed(range(m.bit_length())):
            right_idx = idx + (1 << i)
            if right_idx <= m and ans1 + tr1[right_idx] < k:
                idx = right_idx
                ans1 += tr1[idx]  
                ans2 += tr2[idx]  
        # b[idx + 1]是中位数  sum是区间和 
        # ans2是lsum
        # ans1是前半部分的个数
        # l * x - lsum + rsum - r * x = (2l - len) * x + (total - 2 * lsum)
        return (ans1 * 2 - len) * b[idx + 1] + sum - ans2 * 2

    l = 0
    res = 1
    for r in range(n):
        update(a[r], 1)
        while l < r and calc(r - l + 1) > k:
            update(a[l], -1)
            l += 1
        res = max(res, r - l + 1)

    print(res)

    return

"""