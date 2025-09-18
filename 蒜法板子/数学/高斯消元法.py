n=int(input())
eps=1e-8
a=[list(map(float,input().split())) for _ in range(n)]
def gauss():
    r=0
    for c in range(n):
        t=r
        for i in range(r,n):
            if abs(a[i][c])>abs(a[t][c]):
                t=i
        if abs(a[t][c])<eps:
            continue
        for i in range(c,n+1):
            a[t][i], a[r][i] = a[r][i], a[t][i]  # 将绝对值最大的换到最顶端
        for i in range(n,c-1,-1):
            a[r][i]/=a[r][c]
        for i in range(r+1,n):
            if abs(a[i][c])>eps:
                for j in range(n, c-1, -1):
                    a[i][j] -= a[r][j] * a[i][c]
        r+=1
    if r<n:
        for i in range(r,n):
            if abs(a[i][n])>eps:
                return 2        # 无解
        return 1                # 有无穷多解
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            a[i][n] -= a[i][j] * a[j][n]
    return 0    # 有唯一解
ans = gauss()
if ans == 0:
    for i in range(n):
        if abs(a[i][n]) < eps:
            a[i][n] = 0
        print("{:.2f}".format(a[i][n]))
elif ans == 1:
    print("Infinite group solutions")
else:
    print("No solution")

