# 理论基础：https://oi-wiki.org/graph/min-cycle/
# LC:https://leetcode.cn/problems/shortest-cycle-in-a-graph/description/
"""
返回图中 最短环的长度。如果不存在环，则返回 -1 。
1.枚举每个起点BFS找最短环  O(nm)
2.可以枚举每一条边, 然后删除这条边u-v(删除了u仍然可以到v说明有环)，然后用求最短路。 O(m^2)
边权不是1的时候就不可以用bfs了, 可以改用最短路算法

"""
from collections import deque
from typing import List
inf = float('inf')
# 1。枚举起点O(nm)
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        res = -1
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        def bfs(i):
            res = inf
            dis = [-1] * n
            dis[i] = 0
            q = deque([(i, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] == -1:  # 没访问过
                        dis[y] = dis[x] + 1
                        q.append((y, x))   
                    elif y != fa:   # 访问过，并且不是父亲节点，存在环，但不一定是最小的环
                        res = min(res, dis[x] + dis[y] + 1)
            return res
        res = min(bfs(i) for i in range(n))
        return res if res != inf else -1

# 枚举删除边O(m^2)
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        res = -1
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        def bfs(st, ed):
            dis = [-1] * n   # 记录距离
            dis[st] = 0
            q = deque([st])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if dis[y] == -1:   # 未访问过
                        if x == st and y == ed:  # 不走删除的边
                            continue
                        q.append(y)
                        dis[y] = dis[x] + 1
            return inf if dis[ed] == -1 else dis[ed] + 1
        res = inf
        for x, y in edges:  # 枚举删除哪条边
            res = min(res, bfs(x, y))
        return -1 if res == inf else res