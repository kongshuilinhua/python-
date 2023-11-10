'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-06 15:26:33
LastEditors: ElysiaRealme
Language: Python
'''

"""

def spfa():
    dis = [inf] * (n+ 1)
    dis[1] = 0
    s = set()
    s.add(1)      # 记录哪些点被更新过， 只有前驱结点变小了，后续的结点才能变小
    q = deque([1])
    while q:
        node = q.popleft()
        s.remove(node)     # 可以重复更新
        for y, w in g[node]:
            if dis[y] > dis[node] + w:
                dis[y] = dis[node] + w
                if y not in s:
                    q.append(y)
                    s.add(y)
    return dis[n] if dis[n] != inf else "impossible"

for _ in range(m):
    a, b, w = MII()
    g[a].append((b, w))

"""