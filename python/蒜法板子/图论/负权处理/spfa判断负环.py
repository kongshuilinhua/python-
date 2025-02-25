"""
n, m = MII()
g = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
def spfa():
    dis = [0] * (n + 1)   # 初始化为0
    s = set()
    q = deque([i for i in range(1, n + 1)]) # 环的起点不确定，所以全部入队
    for i in range(1, n + 1):
        s.add(i)
    while q:
        node = q.popleft()
        s.remove(node)     # 可以重复更新
        for y, w in g[node]:
            if dis[y] > dis[node] + w:
                dis[y] = dis[node] + w
                cnt[y] = cnt[node] + 1
                if cnt[y] >= n:   # 有n条边, 说明有n+1个点, 重复了说明有环
                    return True
                if y not in s:
                    q.append(y)
                    s.add(y)
    return False

for _ in range(m):
    a, b, w = MII()
    g[a].append((b, w))
print("Yes" if spfa() else "No")

"""