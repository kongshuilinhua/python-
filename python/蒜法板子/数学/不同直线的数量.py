
# https://ac.nowcoder.com/acm/contest/78309/I
# https://leetcode.cn/problems/max-points-on-a-line/
# 手写的gcd特性一正一负的数字返回后一个，而官方gcd是返回的正数，这样不用特判
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
# def solve():
#     n = II()
#     if n == 1:
#         print(0)
#         return
#     points = [LII() for _ in range(n)]
#     d = defaultdict(int)
#     for i in range(n):
#         for j in range(i + 1, n):
#             x1, y1 = points[i]
#             x2, y2 = points[j]
#             a = y1 - y2
#             b = x2 - x1
#             if a == 0 and b == 0:
#                 print("inf")
#                 return
#             c = x1 * y2 - x2 * y1
#             g = gcd(gcd(a, b), c)
            
#             d[(a // g, b // g, c // g)] += 1
#     res = len(d)
#     print(res if res else "inf")


#     return



