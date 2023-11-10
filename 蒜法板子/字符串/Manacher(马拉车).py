# 线性时间计算最长的回文子串
s1 = input()
P = [0] * 114514
s2 = "^"
for i in range(len(s1)):
    s2 += '#'
    s2 += s1[i]
s2 += '#@'
r = mid = 0
for i in range(1, len(s2) - 1):
    P[i] = min(P[2 * mid - i], r - i) if r > i else 1  # 进行三种情况的判断
    while s2[i + P[i]] == s2[i - P[i]]: P[i] += 1       # 中心扩展
    if i + P[i] > r:                # 如果当前回文串已经覆盖到了原先没有覆盖到的地方，则更新标记
        r = i + P[i]
        mid = i
print(max(P) - 1)
