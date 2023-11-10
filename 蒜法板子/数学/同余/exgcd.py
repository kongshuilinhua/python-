'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-10-13 15:34:09
LastEditors: ElysiaRealme
Language: Python
'''

# https://www.acwing.com/solution/content/1393/这篇题解帮助理解证明

def exgcd(a, b, x, y):
    if b == 0:   # b=0时, ax + by = a, 因此x=1, y=0
        return a, 1, 0
    d, y, x = exgcd(b, a % b, y, x)
    y -= a // b * x
    return d, x, y

    