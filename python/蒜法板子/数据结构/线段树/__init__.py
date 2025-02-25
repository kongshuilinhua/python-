# 把区间表示为若干区间的并集
class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(1, 1, self.n)

    def _build(self, o, l, r):
        if l == r:
            self.tree[o] = self.nums[l - 1] # 数据的下标从1开始，线段树也是从1开始。直接传入数组，不要加[0]
            return
        mid = l + r >> 1
        self._build(o * 2, l, mid)
        self._build(o * 2 + 1, mid + 1, r)
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
    
    def _query(self, o, l, r, L, R):  # 求[L, R] 范围内的元素和
        if L <= l and r <= R:
            return self.tree[o]
        tree = 0
        mid = (l + r) // 2
        if L <= mid:
            tree += self._query(o * 2, l, mid, L, R)
        if R > mid:
            tree += self._query(o * 2 + 1, mid + 1, r, L, R)
        return tree
    
    def _update(self, o, l, r, idx, val):  # 当前结点和它表示的区间, 需要给idx对应下标+val
        if l == r:  # 递归到了叶子，一定等于idx，直接加
            self.tree[o] += val
            return
        mid = (l + r) // 2
        if idx <= mid:  # 往左子树递归
            self._update(o * 2, l, mid, idx, val)
        else:  # 往左子树递归
            self._update(o * 2 + 1, mid + 1, r, idx, val)
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]  # 维护上面的区间

    def query(self, l, r):
        return self._query(1, 1, self.n, l, r)

    def update(self, idx, val):
        return self._update(1, 1, self.n, idx, val)
        
        

        