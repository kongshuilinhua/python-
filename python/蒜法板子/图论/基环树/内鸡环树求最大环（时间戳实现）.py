# https://leetcode.cn/problems/longest-cycle-in-a-graph/description/
def longestCycle(edges):
    n = len(edges)
    time = [0] * n
    clock = 1
    res = -1
    cnt = 0
    for i in range(n):
        if time[i]:continue
        start_time = clock
        cnt += 1
        x = i
        while x != -1:
            if time[x]:
                if time[x] >= start_time:
                    res = max(res, clock - time[x])
                break
            time[x] = clock
            clock += 1
            x = edges[x]
    return res

from typing import List
from collections import deque
# https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/
# https://atcoder.jp/contests/abc357/tasks/abc357_e
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        rg = [[] for _ in range(n)]
        left = [0] * n
        for i, x in enumerate(edges):
            rg[x].append(i)
            left[x] += 1
        q = deque(i for i, x in enumerate(left) if x == 0)
        # 删除枝
        while q:
            x = q.popleft()
            y = edges[x]
            left[y] -= 1
            if left[y] == 0:
                q.append(y)

        res = [0] * n
        def dfs(x, d):
            res[x] = d
            for y in rg[x]:
                if left[y] == 0:   # 枝上的度数都是0
                    dfs(y, d + 1)
        for i, x in enumerate(left):
            if x <= 0:    # 访问
                continue
            x = i
            ring = []
            # 找出环上的点
            while True:
                left[x] = -1  # 标记已经访问过的
                ring.append(x)
                x = edges[x]
                if x == i:
                    break
            for x in ring:
                dfs(x, len(ring))
        return res