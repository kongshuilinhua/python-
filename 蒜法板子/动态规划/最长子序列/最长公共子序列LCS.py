"""
给定两个长度分别为 N和 M的字符串 A和 B，
求既是 A的子序列又是 B的子序列的字符串长度最长是多少。
"""


# O(n2)dp做法
def LCS(s1, s2):
    n, m = len(s1), len(s2)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:                 # 字母相同，由上一个状态转移过来
                f[i + 1][j + 1] = f[i][j] + 1
            else:                      # 字母不相同，上两种状态取最大值
                f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1])
    print(f[n][m])
