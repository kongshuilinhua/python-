
class LazySegmentTree:
    
    def __init__(self, nums) -> None:
        self.n = len(nums)
        N = 4 * self.n
        self.nums = nums
        self.lazy = [0] * N
        self.sum = [0] * N
        self.build(1, 1, self.n)
        

    def pushup(self, o):  # 子节点更新父结点
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    def pushdown(self, o, l, r):
        if self.lazy[o]:
            self.lazy[o * 2] += self.lazy[o]    # 懒标记传递给子节点
            self.lazy[o * 2 + 1] += self.lazy[o]
            mid = l + r >> 1
            self.sum[o * 2] += (mid - l + 1) * self.lazy[o]  # 维护子节点的区间和
            self.sum[o * 2 + 1] += (r - mid) * self.lazy[o]
            self.lazy[o] = 0      # 清除标记

    def build(self, o, l, r):
        if l == r:
            self.sum[o] = self.nums[l - 1] # 传进来的数据是从1开始的，所以要减1。根据数据更改
            return
        mid = l + r >> 1
        self.build(o * 2, l, mid)
        self.build(o * 2 + 1, mid + 1, r)
        self.pushup(o) # 更新结点信息

    def _update(self, o, l, r, L, R, val):
        if l >= L and r <= R:
            self.sum[o] += (r - l + 1) * val
            self.lazy[o] += val
            return
        self.pushdown(o, l, r)   # 只要有分裂就要pushdown，保证lazy标记的一致性，否则会出错
        mid = l + r >> 1
        if L <= mid:
            self._update(o * 2, l, mid, L, R, val)
        if R > mid:
            self._update(o * 2 + 1, mid + 1, r, L, R, val)
        self.pushup(o)

    def _query(self,o, l, r, L, R):
        res = 0
        if l >= L and r <= R:
            return self.sum[o]
        self.pushdown(o, l, r)  
        mid = l + r >> 1
        if L <= mid:
            res += self._query(o * 2, l, mid, L, R)
        if R > mid:
            res += self._query(o * 2 + 1, mid + 1, r, L, R)
        return res

    def query(self, l, r):
        return self._query(1, 1, self.n, l, r)

    def update(self, l, r, val):
        return self._update(1, 1, self.n, l, r, val)


