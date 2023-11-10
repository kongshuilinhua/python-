def longestCycle(edges):
    n = len(edges)
    time = [0] * n
    clock = 1
    res = -1
    cnt = 0
    for i in range(n):
        if time[i]:continue
        start_time = clock
        cnt += 1
        x = i
        while x != -1:
            if time[x]:
                if time[x] >= start_time:
                    res = max(res, clock - time[x])
                break
            time[x] = clock
            clock += 1
            x = edges[x]
    return res
