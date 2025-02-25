# 归并排序模板+求逆序对
def merge_sort(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    a = arr[:mid]
    b = arr[mid:]
    cnt = merge_sort(a) + merge_sort(b)
    i, n = 0, len(a)
    for x in b:   # 根据需求修改这一段
        while i < n and a[i] <= x:   # 左右已经有序，找到左边第一个比右边大的
            i += 1
        cnt += n - i
    cur = i = j = 0
    m = len(b)
    while True:
        if i == n:
            arr[cur:] = b[j:]
            break
        if j == m:
            arr[cur:] = a[i:]
            break
        if a[i] < b[j]:
            arr[cur] = a[i]
            cur += 1
            i += 1
        else:
            arr[cur] = b[j]
            cur += 1
            j += 1
    return cnt


n = int(input())
a = list(map(int, input().split()))
res = merge_sort(a)
print(res)
