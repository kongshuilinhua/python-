
# ACWING 模板
from typing import List

N = 100010
n, m = map(int, input().split())
h, e, ne = [-1] * N, [0] * N, [0] * N
idx = 0
q, d = [0] * N, [0] * N


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def topsort():
    hh, tt = 0, -1
    for i in range(1, n + 1):
        if d[i] == 0:
            tt += 1
            q[tt] = i
    while hh <= tt:
        t = q[hh]
        hh += 1
        i = h[t]
        while i != -1:
            j = e[i]
            d[j] -= 1
            if d[j] == 0:
                tt += 1
                q[tt] = j
            i = ne[i]
    return tt == n - 1


for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)
    d[b] += 1
print(" ".join(map(str, q[:n])) if topsort() else -1)

# LC模板
from collections import deque
# n是有几个点
def topsort(edges):
    n = k = len(edges)
    g = [[] for _ in range(k)]
    left = [0] * k
    for x, y in edges:
        x -= 1
        y -= 1
        g[x].append(y)
        left[y] += 1
    order = []
    q = deque(i for i, v in enumerate(left) if v == 0)
    while q:
        x = q.popleft()
        order.append(x)
        for y in g[x]:
            left[y] -= 1
            if left[y] == 0:
                q.append(y)
    return order if len(order) == k else None


## 附上一个调用库函数的
from graphlib import TopologicalSorter


def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    def get_pos(cons: List[List[int]]) -> List[int]:
        ts = TopologicalSorter()
        for x in range(1, k + 1):
            ts.add(x)
        for x, y in cons:
            ts.add(y, x)
        pos = [0] * (k + 1)
        for i, x in enumerate(ts.static_order()):
            pos[x] = i
        return pos

    try:
        book = {(i, j): x for x, (i, j) in enumerate(zip(get_pos(rowConditions), get_pos(colConditions)))}
        return [[book.get((i, j), 0) for j in range(k)] for i in range(k)]
    except:
        return []
