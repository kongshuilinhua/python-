'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
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
