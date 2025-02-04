
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


# 可以看食物链这道题
"""
N = int(2e5 + 10)
sys.setrecursionlimit(N)
dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, -1, 1, 1]
inf = float('inf')
n, q = MII()
p = [i for i in range(N)]
dis = [0] * (N)
def find(x):
    if x != p[x]:
        t = p[x]
        p[x] = find(p[x]) 
        dis[x] += dis[t]  # 自己到父结点的距离+父结点到根的距离（递归）=自己到根的距离
    return p[x]
cnt = 0
res = []
for i in range(1, q + 1):
    x, y, w = MII()
    a, b = find(x), find(y)
    if a != b or dis[x] - dis[y] == w:
        res.append(i)
        p[a] = b
        dis[a] = dis[y] - dis[x] + w  # 更新距离
print(*res)

"""