"""
# mlogn m:边数， n:点数
def dijkstra(start, end):
    dis = [inf] * (n + 1)
    dis[start] = 0
    heap = []
    heappush(heap, (0, start))  # 起始点
    while heap:
        d, node = heappop(heap)   #当前距离， 点
        if dis[node] != inf:
            continue
        for y, w in g[node]:  # 更新所有点
            if dis[y] > d + w:
                dis[y] = d + w
                heappush(heap, (dis[y], y))
    return -1 if dis[end] == inf else dis[end]   # 终点


res = dijkstra()
print(res)
"""

