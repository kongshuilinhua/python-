# 单向搜索点指数级增加，改成双向的之后可以降低搜索的范围
# a ^ 10 -> 2 * a ^ 5

from collections import defaultdict, deque

A, B = input().split()
a = []
b = []
while True:
    try:
        x, y = input().split()
        a.append(x)
        b.append(y)
    except:
        break


def extend(q, da, db, a, b):
    d = da[q[0]]
    while q and da[q[0]] == d:   # 判断是否是同一层的点，因为要每次都扩展一层
        s = q.popleft()
        if s in db:           # 没转移就到了，返回距离
            return da[s] + db[s]
        for i in range(len(s)):  # 枚举长度
            for j in range(len(a)):  # 枚举可替换的字串
                if s[i:i + len(a[j])] == a[j]:
                    to_str = s[:i] + b[j] + s[i + len(a[j]):]  # 转移到的状态
                    if to_str in db:  # 成功相遇
                        return da[s] + 1 + db[to_str]
                    if to_str in da:  # 搜过了这个状态
                        continue
                    da[to_str] = da[s] + 1  # 记录距离，入队
                    q.append(to_str)
    return 11


def bfs():
    if A == B:
        return 0
    qa, qb = deque([A]), deque([B])
    da, db = defaultdict(int), defaultdict(int)
    da[A] = db[B] = 0
    while qa and qb:  # 两边都能扩展
        if len(qa) < len(qb):  # 先扩展点少的
            t = extend(qa, da, db, a, b, )
        else:
            t = extend(qb, db, da, b, a)
        if t <= 10:
            return t
    return 11


res = bfs()
print(res if res <= 10 else "NO ANSWER!")
