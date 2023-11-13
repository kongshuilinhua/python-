'''
Descripttion: your project
version: 1.0
Author: ElysiaRealme
Date: 2023-09-09 21:08:08
LastEditors: ElysiaRealme
Language: Python
'''
"""
维护一个字符串集合，支持两种操作：
I x 向集合中插入一个字符串 x
Q x 询问一个字符串在集合中出现了多少次。
"""

from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)


class Trie:
    __slots__ = 'root', 'cnt'

    def __init__(self):
        self.root = Node()
        self.cnt = defaultdict(int)

    # 向树中插入字符串
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            cur = cur.children[w]
        self.cnt[cur] += 1  # 出现的次数+1

    # 向树中搜寻字符串
    def search(self, word: str) -> int:
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur is None:  # 不存在
                return 0
        return self.cnt[cur]  # 存在几个

    # 查询prefix是否是树中字符串的前缀（prefix是否完整的存在树中）
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur is None:
                return False
        return True


n = int(input())
tree = Trie()
for _ in range(n):
    op, s = input().split()
    if op == 'I':
        tree.insert(s)
    else:
        res = tree.search(s)
        print(res)



