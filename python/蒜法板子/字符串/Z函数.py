
"""
Z函数(扩展KMP)
对于长度为n的字符串s, Z函数是一个长度为n的数组,其中第i个元素Z[i]表示s与s[i:]的最长公共前缀(LCP)的长度。
时间复杂度是O(n)
"""
# https://oi-wiki.org//string/z-func/


def z_function(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        if i <= right and z[i - left] < right - i + 1:  
            z[i] = z[i - left]         # 盒内加速
        else:
            z[i] = max(0, right - i + 1) # 盒外暴力
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    return z