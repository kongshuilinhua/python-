def getlcp(s):
    n = len(s)
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):   # 从s[i:]开始的和从s[j:]的最长前缀
            if s[i] == s[j]:
                lcp[i][j] = lcp[i + 1][j + 1] + 1