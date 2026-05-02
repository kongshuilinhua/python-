# 最多匹配多少个子序列
# https://ac.nowcoder.com/acm/contest/71512/G

"""
n = II()
s = I()
n = len(s)
suf = [0] * (n + 10)
p1 = "ikod"
p2 = "kira"
j = 0
for i in range(n - 1, -1, -1):
    suf[i] = suf[i + 1]
    if p1[j] == s[i]:
        j += 1
        if j == 4:
            j = 0
            suf[i] += 1
j = 0
res = 0
cnt = 0
for i, c in enumerate(s):
    if p2[j] == c:
        j += 1
        if j == 4:
            j = 0
            cnt += 1
            if suf[i + 1]:
                res = max(res, cnt + suf[i + 1])
print(res * 4)
"""