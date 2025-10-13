n = 0
a = []
f = []
for i in range(n):
    bit = 1 << i
    for j in range(1 << i):
        f[j | bit] = f[j] + a[i]