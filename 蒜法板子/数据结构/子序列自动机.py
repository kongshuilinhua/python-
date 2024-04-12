# dp[i][0~25]储存每个字母后续首先出现的位置，这样转移的时候可以直接跳而不用顺序遍历s串，复杂度只跟目标串t有关。
# 初始化复杂度O(n),n是s串长度。查询复杂度是O(W),W是目标串的总长度。
class SubSequenceAuto:
    def __init__(self, s, abc='abcdefghijklmnopqrstuvwxyz'):
        self.s, self.abc = s, abc
        self.n, abc_len = len(s), len(abc)
        self.abc_index = {v:k for k, v in enumerate(abc)}  # 离散化坐标
        self.dp = dp = [[self.n] * abc_len for _ in range(self.n + 1)]  # 不存在的话就是n     
        
        for i in range(self.n - 1, -1, -1):
            dp[i] = dp[i + 1][:]
            dp[i][self.abc_index[s[i]]] = i   # 更新当前位置的字母的位置
            # for j in range(abc_len):
            #     dp[i][j] = i if s[i]==abc[j] else dp[i+1][j] 
            
    def query_is_sub_seq(self, t, r=0):
        dp, abc_index, n = self.dp, self.abc_index,self.n
        for c in t:
            r = dp[r][abc_index[c]]
            if r == n:
                return 0   # 未找到
            r += 1
        return r    # 第一次出现的终止位置