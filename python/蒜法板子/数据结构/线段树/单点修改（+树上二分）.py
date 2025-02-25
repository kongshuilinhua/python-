# LC2286
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.sum = [0] * (4 * n)
        self.min = [0] * (4 * n)

    def add(self, o, l, r, idx, val):  # 当前结点和它表示的区间, 需要给idx对应下标+val
        if l == r:  # 递归到了叶子，一定等于idx，直接加
            self.sum[o] += val
            self.min[o] += val
            return
        mid = (l + r) // 2
        if idx <= mid:  # 往左子树递归
            self.add(o * 2, l, mid, idx, val)
        else:  # 往左子树递归
            self.add(o * 2 + 1, mid + 1, r, idx, val)
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]  # 维护上面的区间
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])

    def query_sum(self, o, l, r, L, R):  # 求[L, R] 范围内的元素和
        if L <= l and r <= R:
            return self.sum[o]
        sum = 0
        mid = (l + r) // 2
        if L <= mid:
            sum += self.query_sum(o * 2, l, mid, L, R)
        if R > mid:
            sum += self.query_sum(o * 2 + 1, mid + 1, r, L, R)
        return sum

    # 返回[1, R] 范围内的 <= val 的最小下标， 不存在就返回0
    def index(self, o, l, r, R, val):
        if self.min[o] > val:
            return 0
        if l == r:
            return l
        mid = (l + r) // 2
        if self.min[o * 2] <= val:
            return self.index(o * 2, l, mid, R, val)
        if R > mid: 
            return self.index(o * 2 + 1, mid + 1, r, R, val)
        return 0

    def gather(self, k: int, maxRow: int):
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
        if i == 0:
            return []
        seats = self.query_sum(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        left = (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1)
        if left < k:
            return False
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)
        while True:
            left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
            if k <= left_seats:
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
