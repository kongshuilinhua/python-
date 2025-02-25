N = int(1e5 + 10)
n, m = map(int, input().split())
color = [0] * N
g = [[] for _ in range(N)]


def dfs(u, col):
    color[u] = col  # 染色当前点
    for v in g[u]:  # 遍历相邻点
        if not color[v]: # 如果没染色
            if not dfs(v, 3 - col): # 递归失败
                return False
        elif color[v] == col:   # 相邻点的颜色和当前点相同
            return False
    return True


for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
flag = True
for i in range(1, n + 1):
    if not color[i]:  # 未染色
        if not dfs(i, 1):  # 染色失败，直接退出
            flag = False
            break
if flag:
    print("Yes")
else:
    print("No")
k = 2