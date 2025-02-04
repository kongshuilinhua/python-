'''
Descripttion: LCA 
version: 1.0
Author: ElysiaRealme
Date: 2023-10-03 12:51:27
LastEditors: ElysiaRealme
Language: Python
'''
from typing import *
from collections import deque

# 下标从0开始
class TreeAncestor:
    def __init__(self, g, root=0):
        n = len(g)
        m = n.bit_length()
        depth = [0] * n
        fa = [[-1] * m for _ in range(n)]
        def bfs(root):
            q = deque([(root, -1, 0)])
            while q:
                x, father, cur_depth = q.popleft()
                depth[x] = cur_depth
                fa[x][0] = father
                for y in g[x]:
                    if y != father:
                        q.append((y, x, cur_depth + 1))

        bfs(root)
        for i in range(m - 1):
            for x in range(n):   # 下标从1开始记得改这里
                p = fa[x][i]
                if p != -1:
                    fa[x][i + 1] = fa[p][i]
        self.depth = depth
        self.fa = fa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                node = self.fa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.fa[x]) - 1, -1, -1):  # 从大到小枚举，能跳就跳
            px, py = self.fa[x][i], self.fa[y][i]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return self.fa[x][0]
