'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-20 16:18:01
LastEditors: ElysiaRealme
Language: Python
'''
from collections import deque
class MyQueue: #单调队列（从大到小
    def __init__(self):
        self.queue = deque() #使用list来实现单调队列
    
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()#list.pop()时间复杂度为O(n),这里可以使用collections.deque()
            
    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]
    

"""
# LC 239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            while q and i - q[0] + 1 > k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

"""