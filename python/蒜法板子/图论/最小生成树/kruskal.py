"""
inf = float('inf')
n, m = MII()
g = []
p = [i for i in range(n + 1)]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

for _ in range(m):
    a, b, w = MII()
    g.append((a, b, w))
g.sort(key=lambda x:x[2])
res = cnt = 0
for i in range(m):
    a, b, w = g[i]
    a, b = find(a), find(b)
    if a != b:
        p[a] = b
        res += w
        cnt += 1
print(res if cnt == n - 1 else "impossible")
"""