from bisect import bisect
from typing import List


# LC2736
class Node:
    __slots__ = "l", "r", "mid", "val", "left", "right"

    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.val = -1
        self.left = None
        self.right = None


def pushUp(node: Node):
    node.val = max(node.left.val, node.right.val)


def pushDown(node: Node):
    if node.left is None:
        node.left = Node(node.l, node.mid)
    if node.right is None:
        node.right = Node(node.mid + 1, node.r)


class Seg:
    def __init__(self):
        self.root = Node(0, int(1e9))

    def update(self, x, val, node: 'Node' = None):
        if node is None:
            node = self.root
        if node.l == x and node.r == x:
            node.val = max(node.val, val)
            return
        pushDown(node)
        if x <= node.mid:
            self.update(x, val, node.left)
        else:
            self.update(x, val, node.right)
        pushUp(node)

    def query(self, l, r, node: 'Node' = None):
        if node is None:
            node = self.root
        if l <= node.l and node.r <= r:
            return node.val
        pushDown(node)
        ans = -1
        if l <= node.mid:
            ans = max(ans, self.query(l, r, node.left))
        if r > node.mid:
            ans = max(ans, self.query(l, r, node.right))
        return ans


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], q: List[List[int]]) -> List[int]:
        n = len(nums1)
        s = []
        for i in range(n):
            s.append([nums1[i], nums2[i], nums1[i] + nums2[i]])
        s.sort()
        seg = Seg()
        r = n - 1
        for i in range(len(q)):
            q[i].append(i)
        q.sort(reverse=True)
        ans = [-1] * len(q)
        for x, y, i in q:
            k = bisect.bisect_left(s, [x, -1, -1])
            if k == n:                              #没有nums1满足nums1[i]>=x
                continue
            while r >= k:
                seg.update(s[r][1], s[r][2])
                r -= 1
            ans[i] = seg.query(y, int(1e9))
        return ans


