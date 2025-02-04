"""
回文数的数位每增长2,回文数的个数为原来的10倍。
如从个位回文数到百位回文数,个数从9个变为90个。
"""

def get_pal():
    pal = []
    for i in range(1, 400):   # 奇回文， 枚举范围是最大范围的一半上取整，1e5是1e3， 1e4是1e2
        p = i
        x = i // 10
        while x > 0:
            p = p * 10 + x % 10
            x //= 10
        pal.append(p)
        if i < 100:   # 偶回文
            p = x = i
            while x > 0:
                p = p * 10 + x % 10
                x //= 10
            pal.append(p)