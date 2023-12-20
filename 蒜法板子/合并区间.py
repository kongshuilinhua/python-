
def merge(intervals):
    n = len(intervals)
    if n <= 1:
        return intervals
    intervals.sort()
    res = [intervals[0]]
    for i in range(1, n):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])  # 有相交的部分
        else:
            res.append(intervals[i])
    return res
