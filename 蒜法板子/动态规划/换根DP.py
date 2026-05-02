
from typing import *
# 树中第 i 个节点与所有其他节点之间的距离之和。
# 重点是变化量的计算
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]  # g[x] 表示 x 的所有邻居
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = [0] * n
        size = [1] * n  # 注意这里初始化成 1 了，下面只需要累加儿子的子树大小
        def dfs(x: int, fa: int, depth: int) -> None:
            ans[0] += depth  # depth 为 0 到 x 的距离
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    dfs(y, x, depth + 1)  # x 是 y 的父节点
                    size[x] += size[y]  # 累加 x 的儿子 y 的子树大小
        dfs(0, -1, 0)  # 0 没有父节点

        def reroot(x: int, fa: int) -> None:
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    ans[y] = ans[x] + n - 2 * size[y]
                    reroot(y, x)  # x 是 y 的父节点
        reroot(0, -1)  # 0 没有父节点
        return ans
# 换根dp+bitset
# https://www.matiji.net/exam/brushquestion/83/4693/305EE97B0D5E361DE6A28CD18C929AF0
"""
const int N = 3e4;
bitset<N> down[N], up[N];
unordered_map<int, bitset<N>> mp[N];
void solve()
{
    int n;
    cin >> n;
    vi a(n);
    for (auto &x : a)
        cin >> x;
    vvi g(n);
    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    // 自底向上求出down[x]:x的子树内核心成员到x的距离集合
    function<void(int, int)> dfs1 = [&](int x, int fa)
    {
        if (a[x] == 1)
            down[x][0] = 1;
        vi child;
        vector<bitset<N>> bs;
        for (auto y : g[x])
        {
            if (y == fa)
                continue;
            child.push_back(y);
            dfs1(y, x);
            bs.push_back(down[y] << 1);
        }
        int k = child.size();
        if (k)
        {
            vector<bitset<N>> suf(k + 1);
            for (int i = k - 1; i >= 0; i--)
                suf[i] = suf[i + 1] | bs[i];
            down[x] |= suf[0];
            bitset<N> t;
            // 求出x所有子树(除当前子树以外)到x的距离的集合
            for (int i = 0; i < k; i++)
            {
                mp[x][child[i]] = t | suf[i + 1];
                t |= bs[i];
            }
        }
    };
    vi res(n);
    // 自顶向下求出up[x]:x以外的部分到x的距离集合
    function<void(int, int)> dfs2 = [&](int x, int fa)
    {
        res[x] = (up[x] | down[x]).count();
        for (auto y : g[x])
        {
            if (y == fa)
                continue;
            up[y] = (up[x] | mp[x][y]) << 1;
            if (a[x] == 1)
                up[y][1] = 1;
            dfs2(y, x);
        }
    };
    dfs1(0, -1);
    dfs2(0, -1);
    for (int i = 0; i < n; i++)
        cout << res[i] << "\n";
}
"""