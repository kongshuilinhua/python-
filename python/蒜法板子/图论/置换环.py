https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
def min_swaps(arr):
    n = len(arr)
    arrPos = [*enumerate(arr)]
    arrPos.sort(key = lambda it:it[1])
    vis = {i:False for i in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrPos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrPos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
