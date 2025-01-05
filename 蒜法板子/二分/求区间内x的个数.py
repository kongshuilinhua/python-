from collections import defaultdict
from bisect import bisect_left, bisect_right
# 存值的下标，再二分求有多少下标在[l, r]范围内
def get_count(a, l, r, k):
    d = defaultdict(list)
    for i, x in enumerate(a): 
        d[x].append(i + 1)
    res = bisect_right(d[k], r) - bisect_left(d[k], l)