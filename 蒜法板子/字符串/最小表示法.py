# 典型题：https://www.acwing.com/problem/content/139/
# 字符串S可以循环右移，目的是求出S循环同构的所有字符串中字典序最小的字符串
# 可以向左移直接把字符串逆序传进来就行


# O(n)求出字符串的最小字典序表示
"""
def get_min(sec):
    n = len(sec)
    k, i, j = 0, 0, 1
    while k < n and i < n and j < n:
        if sec[(i + k) % n] == sec[(j + k) % n]: # 差位匹配, 遇到不相同的直接跳到不相同的下一个位置继续匹配
            k += 1
        else:
            if sec[(i + k) % n] > sec[(j + k) % n]:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                i += 1
            k = 0
    i = min(i, j)
    sec += sec
    return sec[i:i+n]

"""