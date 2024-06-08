# https://ac.nowcoder.com/acm/contest/83318/A
def min_swaps(a, b):
    n = len(a)
    indices = {v: i for i, v in enumerate(b)}
    a = [indices[v] for v in a]
    swaps = 0
    for i in range(n):
        while i != a[i]:
            a[a[i]], a[i] = a[i], a[a[i]]
            swaps += 1
    return swaps