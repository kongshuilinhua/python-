'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-11 09:57:06
LastEditors: ElysiaRealme
Language: Python
'''
""""
inf = float('inf')
n, m = MII()
N, M = int(1e4 + 10), int(5e4 + 10)
g = [[] for _ in range(N + 1)]

dfn = [0] * N  # 被访问到的实际时间点
low = [0] * N  # 能回到的最高点
id = [0] * N
timestamp = 0
stk = []
in_stk = [False] * N
scc_cnt = top = 0
Size = [0] * N
doubt = [0] * N

def tarjan(u:int):
    global timestamp, scc_cnt
    dfn[u] = low[u] = timestamp = timestamp + 1   # 时间戳，默认相等
    stk.append(u)   # 入栈
    in_stk[u] = True
    for x in g[u]:
        if not dfn[x]:  # 未访问过该结点
            tarjan(x)
            low[u] = min(low[u], low[x])   # 有可能通过该点回到过去
        elif in_stk[x]:
            low[u] = min(low[u], dfn[x])   # 在栈中我们认为栈下面的点时间戳一定是小于当前点的
    if dfn[u] == low[u]:  # 回到了自己
        scc_cnt += 1
        while True:
            y = stk.pop()  # 节点全部出栈
            in_stk[y] = False
            id[y] = scc_cnt  # 结点属于哪个强连通分量
            Size[scc_cnt] += 1  # 连通分量的大小+1
            if y == u:  # 出栈结束
                break
                
for _ in range(m):
    x, y = MII()
    g[x].append(y)

for i in range(1, n + 1):
    if not dfn[i]:
        tarjan(i)

for i in range(1, n + 1):
    for j in g[i]:
        a, b = id[i], id[j]  # scc内部互相可达
        if a != b:
            doubt[a] += 1
            
zeros = sum = 0
for i in range(1, scc_cnt + 1):
    if not doubt[i]:
        zeros += 1
        sum += Size[i]
        if zeros > 1:
            sum = 0
            break
print(sum)


"""