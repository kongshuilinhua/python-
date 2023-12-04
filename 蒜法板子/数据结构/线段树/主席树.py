import bisect


N = 100010

class Node:
    __slots__ = "l", "r", "cnt"

    def __init__(self):
        self.l = 0
        self.r = 0
        self.cnt = 0

def build(l, r):
    global idx
    idx += 1
    p = idx
    if l == r: 
        return p
    mid = l + r >> 1
    tree[p].l = build(l, mid)
    tree[p].r = build(mid+1, r)
    return p

def insert(p, l, r, x):
    global idx
    idx += 1
    q = idx
    tree[q].l, tree[q].r, tree[q].cnt = tree[p].l, tree[p].r, tree[p].cnt
    if l == r:
        tree[q].cnt += 1
        return q
    mid = l + r >> 1
    if x <= mid: 
        tree[q].l = insert(tree[p].l, l, mid, x)
    else: 
        tree[q].r = insert(tree[p].r, mid+1, r, x)
    tree[q].cnt = tree[tree[q].l].cnt + tree[tree[q].r].cnt
    return q
    
def query(q, p, l, r, k):
    if l == r:
        return l
    cnt = tree[tree[q].l].cnt - tree[tree[p].l].cnt
    mid = l + r >> 1
    if k <= cnt:
        return query(tree[q].l, tree[p].l, l, mid, k)
    else:
        return query(tree[q].r, tree[p].r, mid + 1, r, k - cnt)
    


def find(x):
    return bisect.bisect_left(nums, x)

idx = 0
tree = [Node() for _ in range(4 * N + N * 17)]
n, m = map(int, input().split())
a = list(map(int, input().split()))
root = [0] * N
nums = sorted(set(a))
root[0] = build(0, len(nums) - 1)
for i in range(1, n + 1):
    root[i] = insert(root[i - 1], 0, len(nums) - 1, find(a[i - 1]))

for _ in range(m):
    l, r, k = map(int, input().split())
    res = query(root[r], root[l - 1], 0, len(nums) - 1, k)
    print(nums[res])