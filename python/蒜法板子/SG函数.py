# https://oi-wiki.org//math/game-theory/impartial-game/
# 对于状态x和它的所有k个后继状态y1,y2,...,yk，定义SG函数：SG(x)=mex{SG(y1),SG(y2),...,SG(yk)}。
# SG定理：对于n个有向图游戏组成的组合游戏，设它们的起点状态分别为x1,x2,...,xn，那么当且仅当SG(x1)^SG(x2)^...^SG(xn)!=0时，先手必胜。

# 例题
# https://ac.nowcoder.com/acm/contest/87255/C
"""
def solve():
    n = II()
    a = LII()
    @lru_cache(None)
    def sg(x):
        if x <= 0:
            return 0
        s = set()
        for i in range(1, x + 1):
            s.add(sg(x - i))
        for i in range(1, x + 1):
            for j in range(1, x - i):
                s.add(sg(i) ^ sg(j) ^ sg(x - i - j))
        for i in range(1, 114):
            if i not in s:
                return i
    res = reduce(xor, [sg(x) for x in a])
    print('w win' if res else 'W win')

    return
"""

# 集合Nim游戏
# https://www.acwing.com/problem/content/895/
"""

def solve():
    n = II()
    a = LII()
    a.sort()
    m = II()
    b = LII()
    @lru_cache(None)
    def dfs(x):
        s = set()
        for y in a:
            if x >= y:
                s.add(dfs(x - y))
            else:
                break
        for i in range(1000000000):
            if i not in s:
                return i
    res = reduce(xor, [dfs(x) for x in b])
    print("Yes" if res else "No")

"""