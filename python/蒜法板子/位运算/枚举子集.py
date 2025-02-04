def subset(nums):
    n = len(nums)
    s = sub = (1 << n) - 1  # 全集
    res = [nums]

    # 转换
    def bits_mapping(sub):
        string = bin(sub)[2:].zfill(n)
        return [nums[i] for i, x in enumerate(string) if x == '1']

    while sub:
        sub = (sub - 1) & s
        res.append(bits_mapping(sub))
    return res
