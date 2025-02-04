
# 模板：https://www.luogu.com.cn/problem/P4568
# 应用：https://codeforces.com/contest/1915/problem/G

# 有k次免费的机会
"""
# mlogn m:边数， n:点数
def dijkstra(start, end):
    s = set()
    dis = [inf] * (k + 1) * n
    dis[start] = 0
    heap = []
    heappush(heap, (0, start))  # 起始点
    while heap:
        d, node = heappop(heap)   #当前距离， 点
        if node in s:
            continue
        s.add(node)
        for y, w in g[node]:  # 更新所有点
            if dis[y] > d + w:
                dis[y] = d + w
                heappush(heap, (dis[y], y))
    return -1 if dis[end] == inf else dis[end]   # 终点




n, m, k = MII()
st, ed = MII()
g = [[] for _ in range(n * (k + 1))]
for _ in range(m):
    u, v, w = MII()
    g[u].append((v, w))
    g[v].append((u, w))
    for j in range(1, k + 1):
        # 双向边
        g[u + (j - 1) * n].append((v + j * n, 0))    # 当前层到下一层的费用为0, 相当于一次免费的机会
        g[v + (j - 1) * n].append((u + j * n, 0))
        g[u + j * n].append((v + j * n, w))     # 每一层之间连上边，最后每一层都是相同的
        g[v + j * n].append((u + j * n, w))

for i in range(1, k + 1):
    g[ed + (i - 1) * n].append((ed + i * n, 0))  # 终点到下一层的终点费用为0,实际为到任意一层的终点就行了
dis = [[inf] * (k + 1) for _ in range(n)]
res = dijkstra(st, ed + k * n)
print(res)
"""

### 也可以不用加入节点，直接用类似dp的思路
"""



dis = [[inf] * (k + 1) for _ in range(n)]  # dis[i][j] 表示从起点出发, 到i号点, 用了j次免费机会的最短路
dis[st][0] = 0    # 起点到起点的距离为0, 用了0次机会
h = []
vis = set()
heappush(h, (0, st, 0)) # 距离, 点, 用的机会次数
while h:
    _, x, cnt = heappop(h)
    if (x, cnt) in vis:
        continue
    vis.add((x, cnt))
    for y, w in g[x]:
        if cnt < k and dis[y][cnt + 1] > dis[x][cnt]:  # 可以免费通行时经行更新, 更新的思路和dijkstra类似
            dis[y][cnt + 1] = dis[x][cnt]
            heappush(h, (dis[y][cnt + 1], y, cnt + 1))
        if dis[y][cnt] > dis[x][cnt] + w:        # 不可以免费通行时进行更新
            dis[y][cnt] = dis[x][cnt] + w
            heappush(h, (dis[y][cnt], y, cnt))

res = min(dis[ed])
print(res)

"""