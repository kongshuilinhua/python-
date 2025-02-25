# 线性时间计算最长的回文子串
s1 = input()
P = [0] * 114514
s2 = "^"
for i in range(len(s1)):
    s2 += '#'
    s2 += s1[i]
s2 += '#@'
r = mid = 0
for i in range(1, len(s2) - 1):
    P[i] = min(P[2 * mid - i], r - i) if r > i else 1  # 进行三种情况的判断
    while s2[i + P[i]] == s2[i - P[i]]: P[i] += 1       # 中心扩展
    if i + P[i] > r:                # 如果当前回文串已经覆盖到了原先没有覆盖到的地方，则更新标记
        r = i + P[i]
        mid = i
print(max(P) - 1)

class Manacher:
    def __init__(self, string=''):
        self.string = string

    def add_char(self):
        add_string = ['^']
        for char in self.string:
            # add_string += '@' + char
            add_string.append('@')
            add_string.append(char)
        # add_string += '@*'
        add_string.append('@')
        add_string.append('*')
        return "".join(add_string)
    
    def get_p(self): 
        self.add_string = self.add_char()
        self.P = [0] * len(self.add_string)
        R, mid = 0, 0
        for i in range(1, len(self.add_string)-1):
            self.P[i] = min(self.P[mid*2-i], R-i) if R > i else 0
            while self.add_string[i+1+self.P[i]] == self.add_string[i-1-self.P[i]]:
                self.P[i] +=1
            if i + self.P[i] > R:
                R = i + self.P[i]
                mid = i
        return self.P
    
    def check_partition_s(self, l, r): # 判断在串S的区间[l,r]的子串是否为回文串。
        l, r = l * 2 + 2, r * 2 + 2
        mid = (l + r) // 2
        return self.P[mid] > r - mid

