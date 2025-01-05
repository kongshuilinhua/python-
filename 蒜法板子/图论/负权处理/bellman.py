N = 100010
inf = float("inf")
Edge = []  # 存放边
dist = [inf] * N

# 有边数限制的最短路  ->求解经过至多k条边的st到ed的最短距离
def Ballman_Ford():
    dist[1] = 0
    for _ in range(k):
        # 循环k次
        back_up = dist.copy()  # 需要进行备份， 防止更新过的点立刻影响到本次更新
        for j in range(m):      # m条边
            a, b, w = Edge[j]
            dist[b] = min(dist[b], back_up[a] + w)

    if dist[n] == inf:
        return "impossible"
    else:
        return dist[n]


n,m,k = map(int,input().split())
for _ in range(m):
    a,b,c = map(int,input().split())
    Edge.append([a,b,c])

print(Ballman_Ford())

