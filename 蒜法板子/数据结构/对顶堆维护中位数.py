class Median:
    def __init__(self) -> None:
        self.l = SortedList()
        self.r = SortedList()
        self.less = self.greater = 0
    
    def Add(self, x):
        n, m = len(self.l), len(self.r)
       # print(self.l, self.r, n, m)
        if n == m:
            if n == 0 or x < self.r[0]:
                self.l.add(x)
                self.less += x
            else:
                t = self.r[0]
                self.r.remove(t)
                self.r.add(x)
                self.greater += x - t
                self.l.add(t)
                self.less += t
        else:
            if self.l[-1] <= x:
                self.r.add(x)
                self.greater += x
            else:
                t = self.l[-1]
                self.l.remove(t)
                self.l.add(x)
                self.less += x - t
                self.r.add(t)
                self.greater += t
    
    def Remove(self, x):
        f1 = self.l.count(x)
        f2 = self.r.count(x)
        n, m = len(self.l), len(self.r)
        if f1 and f2:
            if n <= m:
                self.r.remove(x)
                self.greater -= x
            elif n > m:
                self.l.remove(x)
                self.less -= x
        elif f1:
            self.l.remove(x)
            self.less -= x
            if len(self.l) < len(self.r):
                t = self.r[0]
                self.greater -= t
                self.r.remove(t)
                self.l.add(t)
                self.less += t
        elif f2:
            self.r.remove(x)
            self.greater -= x
    
    def calc(self):
        mid = self.l[-1] if self.l else self.r[0]
        n, m = len(self.l), len(self.r)
        return n * mid - self.less + self.greater - m * mid




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