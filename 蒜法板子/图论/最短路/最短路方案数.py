# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/
# 最短路的方案数
from heapq import heappop, heappush
from typing import List
from math import inf

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        g = [[] for _ in range(n)]
        for x, y, w in roads:
            g[x].append((y, w))
            g[y].append((x, w))
        dis = [inf] * n
        dis[0] = 0
        cnt = [0] * n
        cnt[0] = 1
        h = [(0, 0)]
        s = set()
        while h:
            d, node = heappop(h)
            if node in s:
                continue
            s.add(node)
            for y, w in g[node]:
                if dis[y] > d + w:  # 更新最短路
                    dis[y] = d + w
                    heappush(h, (dis[y], y))
                    cnt[y] = cnt[node]
                elif dis[y] == d + w:  # 有多条最短路
                    cnt[y] += cnt[node]
        return cnt[-1] % mod