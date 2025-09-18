
'''
# O(n^3)
N = 210
d = [[float("inf")] * N for _ in range(N)]

for i in range(1, n + 1):
    dis[i][i] = 0

def floyd(): 
    for k in range(1, n + 1):      # 经过结点编号在1-k-1的最短路(插点)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

def add_edge(u, v, w):
    # 插入(u, v, w)后，对所有 i, j 尝试经过这条新边的路径
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i → u → v → j
            d[i][j] = min(d[i][j], d[i][u] + w + d[v][j])
            # 如果是无向图，还可以考虑 i → v → u → j
            # d[i][j] = min(d[i][j], d[i][v] + w + d[u][j])
                
for _ in range(m):
    x, y, z = map(int, input().split())
    d[x][y] = min(d[x][y], z)  # 防止有重边
floyd()
''' 