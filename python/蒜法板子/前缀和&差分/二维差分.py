
# 看图帮助理解https://leetcode.cn/problems/stamping-the-grid/?envType=daily-question&envId=2023-12-14
"""
n, m, q = MII()
a = [[0] * (m + 2) for _ in range(n + 2)]

def insert(x1, y1, x2, y2, c):   
    a[x1][y1] += c
    a[x2 + 1][y1] -= c
    a[x1][y2 + 1] -= c
    a[x2 + 1][y2 + 1] += c

for i in range(1, n + 1):
    row = [0] + LII()        # 下标从1开始
    for j in range(1, m + 1):
        insert(i, j, i, j, row[j])

for _ in range(q):
    x1, y1, x2, y2, c = MII() 
    insert(x1, y1, x2, y2, c)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] += a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        print(a[i][j], end=' ')
    print()

"""