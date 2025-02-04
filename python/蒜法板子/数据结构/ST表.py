
# nlogn区间RMQ问题
# 二维区间RMQ问题：https://www.luogu.com.cn/problem/P2216（暂未整理）


# 下标从0开始[0, n)
class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]

import math
N = 200010
M = 18
f = [[0] * M for _ in range(N)]
n, m =  MII()
a = LII()

for i in range(n):
    f[i][0] = a[i]

def st():  # f[i,j]为以第i个数为起点，长度为2^j的一段区间中的最大值
    for j in range(1, M + 1):
        i = 0
        while i + (1 << j) <= n:   # i - > i+2^j - 1  = 两段 i -> i + 2^(j-1)和i+2^(j-1) - > i+2^j - 1
            f[i][j] = max(f[i][j - 1], f[i + (1 << j - 1)][j - 1])
            i += 1

# 数组下标，查询下标都从0开始
def query(l, r):
    k = int(math.log2(r - l + 1))  # 2 ^ k <= length
    res = max(f[l][k], f[r - (1 << k) + 1][k])  # 可能重叠的两段，下标是0开始的，一段依附l，一段依附r
    return res


st()
for _ in range(m):
    l, r = MII()
    print(query(l, r))