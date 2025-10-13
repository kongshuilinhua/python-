# https://leetcode.cn/problems/majority-element-ii/
def get(nums, k):
    nums = [3, 2, 3]
    k = 3
    cand = []
    def upd(x):
        for i in range(len(cand)):
            if cand[i][0] == x:
                cand[i][1] += 1
                return
        for i in range(len(cand)):
            if cand[i][1] == 0:
                cand[i] = [x, 1]
                return
        if len(cand) < k - 1:
            cand.append([x, 1])
            return
        for i in range(len(cand)):
            if cand[i][1] > 0:
                cand[i][1] -= 1

    for x in nums:
        upd(x)
    res = []
    print(cand)
    for i in range(len(cand)):
        if cand[i][1] > 0:
            cnt = sum(1 for x in nums if x == cand[i][0])
            if cnt > len(nums) // k:
                res.append(cand[i][0])
    return res