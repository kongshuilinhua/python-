"""
# 预处理s[i][j]是否是回文串
g = [[1] * n for _ in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        g[i][j] = g[i + 1][j - 1] and (s[i] == s[j])
"""