
def LCIS(a, b):  # 注意a和b的下标要从1开始
    n = len(a)
    # a = [0] + a
    # b = [0] + b
    # f[i][j]代表a数组的前i个数字，b数组的前j个数字，并且以b[j]为结尾的子序列方案
    f = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        mx = 1
        for j in range(1, n + 1):
            # 不包含a[i]
            f[i][j] = f[i - 1][j]
            # 包含a[i]，找找子序列的倒数第二个数在数组b是第几个数.也就是f[i - 1][j - 1] + 1, f[i - 1][j - 2] + 1一直到f[i - 1][1] + 1的最大值
            # 可以不用每次都遍历寻找，通过一个变量mx记录下前缀最大值
            if a[i] == b[j]:        # 状态转移
                f[i][j] = max(f[i][j], mx)
            if a[i] > b[j]:         # 更新最大值
                mx = max(mx, f[i - 1][j] + 1)
    res = 0
    for i in range(1, n + 1):
        res = max(res, f[n][i])
    return res
