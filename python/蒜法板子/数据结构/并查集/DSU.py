
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

# 递归实现
"""
p = [i for i in range(n + 1)]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


"""

## 迭代实现
"""

def find(x):
    t = x
    while x != p[x]:
        x = p[x]
    while t != x:
        p[t], t = x, p[t]
    return x

"""

