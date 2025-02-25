# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 右  下  左 上
        res = [[-1] * n for _ in range(m)]
        i = j = di = 0
        while head:
            res[i][j] = head.val
            head = head.next
            dx, dy = DIRS[di]
            if (not 0 <= i + dx < m) or (not 0 <= j + dy < n) or res[i + dx][j + dy] != -1:  # 如果越界了更换方向
                di = (di + 1) % 4
            dx, dy = DIRS[di]
            i += dx
            j += dy
        return res
