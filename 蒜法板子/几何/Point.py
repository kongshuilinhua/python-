
import math
eps = 1e-8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __mul__(self, k):
        if isinstance(k, (int, float)):
            return Point(self.x * k, self.y * k)
        # 点积：当右侧为 Point 时
        return self.x * k.x + self.y * k.y

    def __truediv__(self, k):
        return Point(self.x / k, self.y / k)
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    def length(self):
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) <= eps and abs(self.y - other.y) <= eps
