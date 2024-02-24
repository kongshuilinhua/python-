# h[i]前i个字符的hash值
# 字符串变成一个p进制数字，体现了字符+顺序，需要确保不同的字符串对应不同的数字
# P = 131 Q = 32或  13331 Q=2^64，在99%的情况下不会出现冲突
# 使用场景： 两个字符串的子串是否相同

"""

n, m = MII()
s = ' ' + I()
P, Q = 131, 1 << 32
N = 100010
h, p = [0] * N, [1] * N
for i in range(1, n + 1):
    p[i] = p[i - 1] * P % Q  
    h[i] = (h[i - 1] * P + ord(s[i])) % Q  # 字符串前缀和

# 区间和公式的理解: ABCDE 与 ABC 的前三个字符值是一样，只差两位，
# 乘上P的二次方把 ABC 变为 ABC00, 再用 ABCDE - ABC00 得到 DE 的哈希值。
def query(l, r):
    return (h[r] - h[l - 1] * p[r - l + 1]) % Q

for _ in range(m):
    l1, r1, l2, r2 = MII()
    if query(l1, r1) == query(l2, r2):
        print("Yes")
    else:
        print("No")
        
"""