from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.l, self.r = [], []  # 左边大根堆， 右边小根堆

    def addNum(self, x: int) -> None:
        n, m = len(self.l), len(self.r)  # 左右的个数应该相等， 或者左边比右边大一个
        if n == m:
            if n == 0 or x < self.r[0]:   # 都是空的， 或者x比右边的小， 那么就放到左边
                heappush(self.l, -x)
            else:
                heappush(self.l, -heappop(self.r))  # 否则把右边的最小的放到左边， 然后把x放到右边
                heappush(self.r, x)
        else:
            if -self.l[0] <= x:            # 左边比右边多一个， 那么如果x比左边的都大， 那么就放到右边
                heappush(self.r, x)
            else:
                heappush(self.r, -heappop(self.l))  # 否则把左边最大的放到右边， 然后把x放到左边
                heappush(self.l, -x)

    def findMedian(self) -> float:
        n, m = len(self.l), len(self.r)
        if n == m:
            return (-self.l[0] + self.r[0]) / 2
        else:
            return -self.l[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()