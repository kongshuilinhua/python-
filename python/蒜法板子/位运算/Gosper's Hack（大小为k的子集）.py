# LC2397. 被列覆盖的最多行数
# 1.直接枚举所有情况
def maximumRows(mat, cols) -> int:
    mask = [sum(v << j for j, v in enumerate(row)) for row in mat]
    res = 0
    for set in range(1 << len(mat[0])):
        if set.bit_count() != cols:
            continue
        cnt = 0
        for row in mask:
            if row & set == row:
                cnt += 1
        res = max(res, cnt)
    return res


# 2.下一个排列算法

# lowbit，取到最低位的1
def lowbit(x):
    return x & -x


# x = 0101110 的下一个：找到第一个01翻转，并且把后面的1都放到末尾
# y = 0110011
# 左半部分 = x + lb
# 右半部分 = （x ^ (x + lb)）// lb >> 2
# 时间复杂度O(C(n, cols) * m)
def maximumRows(mat, cols) -> int:
    mask = [sum(v << j for j, v in enumerate(row)) for row in mat]
    res = 0
    x = (1 << cols) - 1
    while x < (1 << len(mat[0])):
        res = max(res, sum(row & x == row for row in mask))
        lb = x & -x
        left = x + lb
        right = (x ^ (x + lb)) // lb >> 2
        x = left | right
    return res


# n个里面选k个
def combine(n, k):
    res = []
    x = (1 << k) - 1
    while x < (1 << n):
        res.append([i + 1 for i in range(x.bit_length()) if x >> i & 1])
        lb = x & -x
        left = x + lb
        right = (x ^ (x + lb)) // lb >> 2
        x = left | right
    return res
