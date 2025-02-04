# https://atcoder.jp/contests/abc344/tasks/abc344_e
# https://www.acwing.com/problem/content/description/4964/
# https://ac.nowcoder.com/acm/contest/74362/D
"""

n = II()
a = LII()
next_val = {0: 0}
prev_val = {0: 0}
q = II()


for i in range(n):
    y, x = a[i - 1], a[i]     # 把x插入在y后面
    if i == 0:
        y = 0
    next_val[x] = next_val[y]
    prev_val[next_val[y]] = x
    next_val[y] = x
    prev_val[x] = y

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        y, x = op[1], op[2]
        next_val[x] = next_val[y]
        prev_val[next_val[y]] = x
        next_val[y] = x
        prev_val[x] = y
    else:
        x = op[1]
        next_val[prev_val[x]] = next_val[x]
        prev_val[next_val[x]] = prev_val[x]

x = next_val[0]
res = []
while x != 0:
    res.append(x)
    x = next_val[x]
#print(len(res))
print(*res)

"""
