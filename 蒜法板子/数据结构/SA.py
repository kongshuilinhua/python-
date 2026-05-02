from typing import List, Sequence, Tuple
 
 
def useSA(ords: Sequence[int]) -> Tuple[List[int], List[int], List[int]]:
    """返回 sa, rank, height 数组
    Args:
        ords: 可比较的整数序列
    Returns:
        sa: 每个排名对应的后缀
        rank: 每个后缀对应的排名
        height: 第 i 名的后缀与它前一名的后缀的 `最长公共前缀(LCP)`的长度
    """
    sa = getSA(ords)
    n, k = len(sa), 0
    rank, height = [0] * n, [0] * n
    for i, saIndex in enumerate(sa):
        rank[saIndex] = i
 
    for i in range(n):
        if k > 0:
            k -= 1
        while (
                i + k < n
                and rank[i] - 1 >= 0
                and sa[rank[i] - 1] + k < n
                and ords[i + k] == ords[sa[rank[i] - 1] + k]
        ):
            k += 1
        height[rank[i]] = k
    return sa, rank, height
 
 
# https://leetcode.cn/u/freeyourmind/
def getSA(ords: Sequence[int]) -> List[int]:
    """返回sa数组 即每个排名对应的后缀"""
 
    def inducedSort(LMS: List[int]) -> List[int]:
        SA = [-1] * (n)
        SA.append(n)
        endpoint = buckets[1:]
        for j in reversed(LMS):
            endpoint[ords[j]] -= 1
            SA[endpoint[ords[j]]] = j
        startpoint = buckets[:-1]
        for i in range(-1, n):
            j = SA[i] - 1
            if j >= 0 and isL[j]:
                SA[startpoint[ords[j]]] = j
                startpoint[ords[j]] += 1
        SA.pop()
        endpoint = buckets[1:]
        for i in reversed(range(n)):
            j = SA[i] - 1
            if j >= 0 and not isL[j]:
                endpoint[ords[j]] -= 1
                SA[endpoint[ords[j]]] = j
        return SA
 
    n = len(ords)
    buckets = [0] * (max(ords) + 2)
    for a in ords:
        buckets[a + 1] += 1
    for b in range(1, len(buckets)):
        buckets[b] += buckets[b - 1]
    isL = [1] * n
    for i in reversed(range(n - 1)):
        isL[i] = +(ords[i] > ords[i + 1]) if ords[i] != ords[i + 1] else isL[i + 1]
 
    isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
    isLMS.append(1)
    LMS1 = [i for i in range(n) if isLMS[i]]
    if len(LMS1) > 1:
        SA = inducedSort(LMS1)
        LMS2 = [i for i in SA if isLMS[i]]
        pre = -1
        j = 0
        for i in LMS2:
            i1 = pre
            i2 = i
            while pre >= 0 and ords[i1] == ords[i2]:
                i1 += 1
                i2 += 1
                if isLMS[i1] or isLMS[i2]:
                    j -= isLMS[i1] and isLMS[i2]
                    break
            j += 1
            pre = i
            SA[i] = j
        LMS1 = [LMS1[i] for i in getSA([SA[i] for i in LMS1])]
 
    return inducedSort(LMS1)
 
 
def sa_is(s: Sequence[int], upper: int) -> List[int]:
    """SA-IS, linear-time suffix array construction
    Args:
        s (Sequence[int]): Sequence of integers in [0, upper]
        upper (int): Upper bound of the integers in s
    Returns:
        List[int]: Suffix array
    """
 
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1] if s[0] < s[1] else [1, 0]
 
    sa = [0] * n
    ls = [False] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if s[i] == s[i + 1] else (s[i] < s[i + 1])
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if not ls[i]:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i] + 1] += 1
    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]
 
    def induce(lms):
        for i in range(n):
            sa[i] = -1
        buf = sum_s[:]
        for d in lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l[:]
        sa[buf[s[n - 1]]] = n - 1
        buf[s[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[s[v - 1]]] = v - 1
                buf[s[v - 1]] += 1
        buf = sum_l[:]
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[s[v - 1] + 1] -= 1
                sa[buf[s[v - 1] + 1]] = v - 1
 
    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)
    induce(lms)
 
    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l, r = sorted_lms[i - 1], sorted_lms[i]
            end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
            end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r += 1
                if l == n or s[l] != s[r]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s, rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        induce(sorted_lms)
    return sa
 
 
def rank_lcp(s: Sequence[int], sa: List[int]) -> Tuple[List[int], List[int]]:
    """Rank and LCP array construction
    Args:
        s (Sequence[int]): Sequence of integers in [0, upper]
        sa (List[int]): Suffix array
    Returns:
        Tuple[List[int], List[int]]: Rank array and LCP array
    example:
    ```
    ords = [1, 2, 3, 1, 2, 3]
    sa = sa_is(ords, max(ords))
    rank, lcp = rank_lcp(ords, sa)
    print(rank, lcp)  # [1, 3, 5, 0, 2, 4] [3, 0, 2, 0, 1]
    ```
    """
    n = len(s)
    assert n >= 1
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rank[i] - 1] = h
    return rank, lcp
 
 
_, rank, _ = useSA(list(map(ord, s)))