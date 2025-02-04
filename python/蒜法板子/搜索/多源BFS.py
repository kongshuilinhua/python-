# ACwing173. 矩阵距离  （1 <= N, M <= 1000）
# 题目大意：01矩阵，求每个点到最近的1的曼哈顿距离
# 假设有一个超级源点，下一层是所有的1，BFS可以求出它到所有的1的最近距离
# 实际上不用找出这个源点，因为BFS的二段行（x， x + 1）和单调性。源点的下一层就是所有1的点
# 所有直接把所有为1的点最后队列的第一层入队就行
"""
n, m = MII()
g = [list(I()) for _ in range(n)]
dis = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):      # 所有为1的点入队
        if g[i][j] == '1':
            q.append((i, j))
            dis[i][j] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < m and dis[a][b] == -1:
            dis[a][b] = dis[x][y] + 1
            q.append((a, b))
for i in range(n):
    print(*dis[i])
"""
