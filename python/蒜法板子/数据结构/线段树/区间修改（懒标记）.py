
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


class LazySegTree():
    """
        V:  初始序列，树叶节点
        OP: 左右节点之间的合并操作
        E:  线段树维护的值的幺元。op(e, x) = op(x, e) = x
        Mapping:        父结点的懒标记更新子结点的值
        COMPOSITION:    父结点的懒标记更新子结点的懒标记(合并)
        ID:             更新操作/懒标记的幺元
    """
    __slots__ = ['n', 'log', 'size', 'd', 'lz', 'e', 'op', 'mapping', 'composition', 'identity']

    def __init__(self, V, OP, E, MAPPING, COMPOSITION, ID):
        self.n = len(V)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        self.lz = [ID for i in range(self.size)]
        self.e = E
        self.op = OP
        self.mapping = MAPPING
        self.composition = COMPOSITION
        self.identity = ID
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def _all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if (k < self.size):
            self.lz[k] = self.composition(f, self.lz[k])

    def _push(self, k):
        self._all_apply(2 * k, self.lz[k])
        self._all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.identity

    def set(self, p, x):  # 将 p 处的值更改为 x
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p):  # 获取 p 处的值
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.d[p]

    def prod(self, l, r):  # 区间查询 [l,r]
        r += 1
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (((l >> i) << i) != l):
                self._push(l >> i)
            if (((r >> i) << i) != r):
                self._push(r >> i)
        sml, smr = self.e, self.e
        while (l < r):
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):  # 全区间查询
        return self.d[1]

    def apply_point(self, p, f):  # 单点更新
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def apply(self, l, r, f):  # 区间更新
        r += 1
        assert 0 <= l and l <= r and r <= self.n
        if l == r: return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (((l >> i) << i) != l):
                self._push(l >> i)
            if (((r >> i) << i) != r):
                self._push((r - 1) >> i)
        l2, r2 = l, r
        while (l < r):
            if (l & 1):
                self._all_apply(l, f)
                l += 1
            if (r & 1):
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if (((l >> i) << i) != l):
                self._update(l >> i)
            if (((r >> i) << i) != r):
                self._update((r - 1) >> i)

    def max_right(self, l, g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self._push(l >> i)
        sm = self.e
        while (1):
            while (i % 2 == 0):
                l >>= 1
            if not (g(self.op(sm, self.d[l]))):
                while (l < self.size):
                    self._push(l)
                    l = (2 * l)
                    if (g(self.op(sm, self.d[l]))):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, g):
        r += 1
        assert (0 <= r and r <= self.n)
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self._push((r - 1) >> i)
        sm = self.e
        while (1):
            r -= 1
            while (r > 1 and (r % 2)):
                r >>= 1
            if not (g(self.op(self.d[r], sm))):
                while (r < self.size):
                    self._push(r)
                    r = (2 * r + 1)
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0
