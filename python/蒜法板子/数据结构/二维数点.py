# https://codeforces.com/contest/1974/problem/F

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

from bisect import bisect_left
# x1, y1为左下角坐标，x2, y2为右上角坐标。查询矩形内的点的个数（包括边界）
def solve(pts, qrs):
    n, m = len(pts), len(qrs)
    # 离散化坐标y
    Y = set()
    for x, y in pts:
        Y.add(y)
    for x1, y1, x2, y2 in qrs:
        Y.add(y1)
        Y.add(y2)
    Y = sorted(Y)

    op = []
    for i, (x, y) in enumerate(pts):
        y = bisect_left(Y, y) + 1
        op.append((x, y, i, 0))    # 加点操作
    
    # 矩形面积计算原理：s[x2][y2] + s[x1 - 1][y1 - 1] - s[x1 - 1][y2] - s[x2][y1 - 1]
    for i, (x1, y1, x2, y2) in enumerate(qrs):
        y1 = bisect_left(Y, y1) + 1
        y2 = bisect_left(Y, y2) + 1
        op.append((x2, y2, i, 1))
        op.append((x1 - 1, y1 - 1, i, 1))
        op.append((x1 - 1, y2, i, 2))
        op.append((x2, y1 - 1, i, 2))

    op.sort(key=lambda x:x[0])  # 按照x坐标排序，其余相对位置不变

    bit = FenwickTree([0] * (len(Y) + 10))
    res = [0] * m
    for i, (x, y, idx, t) in enumerate(op):
        if t == 0:
            bit.update(y, 1)
        elif t == 1:
            res[idx] += bit.query(y + 1)
        else:
            res[idx] -= bit.query(y + 1)
    return res
