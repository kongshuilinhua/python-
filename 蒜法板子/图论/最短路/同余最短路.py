# https://www.luogu.com.cn/problem/P3403
# https://ac.nowcoder.com/acm/contest/67742/D
"""
def solve():
    n = II()
    x, y, z = MII()
    if x == 1 or y == 1 or z == 1:
        print(n)
        return
    g = [[] for _ in range(x + 1)]
    # di定义为只通过2, 3操作能够到达的最低楼层p,并且满足p%x=i
    # %x就是表示之后可以跳任意次x层
    # 最短路是在算能不能到达那个层
    for i in range(x):
        g[i].append(((i + y) % x, y))  # 核心在与建图
        g[i].append(((i + z) % x, z))
    s = set()
    dis = [inf] * (x + 1)
    dis[1] = 1
    heap = []
    heappush(heap, (1, 1))  # 起始点
    while heap:
        d, node = heappop(heap)   #当前距离， 点
        if node in s:
            continue
        s.add(node)
        for y, w in g[node]:  # 更新所有点
            if dis[y] > d + w:
                dis[y] = d + w
                heappush(heap, (dis[y], y))
    # 只需要跳到不能再跳了，累加答案
    s = sum((n - dis[i]) // x + 1 for i in range(x) if dis[i] <= n)
    print(s)

    return

"""