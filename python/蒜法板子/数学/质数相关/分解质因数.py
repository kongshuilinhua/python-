
# 根号n的时间复杂度
def div(x):
    res = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            s = 0
            while x % i == 0:
                x //= i
                s += 1
            res.append([i, s])
        i += 1
    if x > 1:                   # 最后可能还剩一个
        res.append([x, 1])
    return res

from collections import Counter
def div(x):
    res = Counter()
    i = 2
    while i * i <= x:
        if x % i == 0:
            s = 0
            while x % i == 0:
                x //= i
                s += 1
            res[i] += s
        i += 1
    if x > 1:                   # 最后可能还剩一个
        res[x] += 1
    return res