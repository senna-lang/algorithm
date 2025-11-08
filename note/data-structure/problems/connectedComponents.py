"""
Union-Findを用いて連結成分の個数を求める

Code 11.4: Union-Find を用いて連結成分の個数を求める

問題:
- N個の頂点とM個の辺からなる無向グラフが与えられる
- このグラフの連結成分の個数を求める

連結成分とは:
- 互いに行き来できる頂点の集合
- 例: {0,1,2}, {3,4}, {5} → 3個の連結成分

アルゴリズム:
1. Union-Findで全ての辺を統合
2. 各頂点の根を調べ、異なる根の個数を数える

時間計算量: O(M α(N)) ≈ O(M)
空間計算量: O(N)
"""


class UnionFind:
    """Union-Find (素集合データ構造)"""

    def __init__(self, n: int) -> None:
        """Union-Find を初期化する"""
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int) -> int:
        """x の根を求める（経路圧縮あり）"""
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x: int, y: int) -> bool:
        """x と y が同じグループに属するかどうか"""
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        """x を含むグループと y を含むグループを併合する"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        # union by size
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x: int) -> int:
        """x を含むグループのサイズ"""
        return self.siz[self.root(x)]


def count_connected_components(N: int, edges: list[tuple[int, int]]) -> int:
    """
    連結成分の個数を求める

    Args:
        N: 頂点数
        edges: 辺のリスト [(a, b), ...]

    Returns:
        連結成分の個数
    """
    # Union-Find を要素数 N で初期化
    uf = UnionFind(N)

    # 各辺に対する処理
    for a, b in edges:
        # a を含むグループと b を含むグループを併合する
        uf.unite(a, b)

    # 集計
    # 各頂点の根が同じなら同じ連結成分
    res = 0
    for x in range(N):
        if uf.root(x) == x:  # x が根なら連結成分の代表
            res += 1

    return res
