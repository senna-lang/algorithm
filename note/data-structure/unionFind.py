"""
Union-Find (素集合データ構造) の実装

Code 11.3: Union-Find の全体実装

Union-Findとは:
- 集合を効率的に管理するデータ構造
- 要素が同じグループに属するか判定
- 2つのグループを併合

主な操作:
- root(x): x の根（代表元）を求める
- issame(x, y): x と y が同じグループか判定
- unite(x, y): x を含むグループと y を含むグループを併合
- size(x): x を含むグループのサイズ

最適化技法:
1. 経路圧縮 (Path Compression): root() で根までの経路を短縮
2. union by size: 小さい木を大きい木に併合

時間計算量: ほぼ O(1) (正確には O(α(N))、α: アッカーマン関数の逆関数)
空間計算量: O(N)
"""


class UnionFind:
    """
    Union-Find (素集合データ構造)

    Attributes:
        par: 親ノードの配列 (par[x] = -1 なら x が根)
        siz: グループのサイズ (根のみ有効)
    """

    def __init__(self, n: int) -> None:
        """
        Union-Find を初期化する

        Args:
            n: 要素数

        初期状態: 各要素が独立したグループ
        {0}, {1}, {2}, ..., {n-1}
        """
        # par[x] = -1 なら x が根
        self.par = [-1] * n
        # siz[x] = x を根とする木のサイズ
        self.siz = [1] * n

    def root(self, x: int) -> int:
        """
        x の根を求める（経路圧縮あり）

        Args:
            x: 要素

        Returns:
            x の属するグループの根（代表元）

        経路圧縮:
        根を求める過程で、経路上の全てのノードを根に直接つなぐ
        これにより次回以降のアクセスが高速化される
        """
        # x が根の場合は x を返す
        if self.par[x] == -1:
            return x
        # 経路圧縮: 親を根に更新しながら再帰的に根を求める
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def isSame(self, x: int, y: int) -> bool:
        """
        x と y が同じグループに属するかどうか判定

        Args:
            x: 要素1
            y: 要素2

        Returns:
            x と y の根が一致するかどうか
        """
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        """
        x を含むグループと y を含むグループを併合する

        Args:
            x: 要素1
            y: 要素2

        Returns:
            併合が行われた場合 True、既に同じグループの場合 False

        union by size:
        小さい木を大きい木に併合することで、木の高さを抑える
        """
        # x, y をそれぞれ根まで移動する
        x = self.root(x)
        y = self.root(y)

        # すでに同じグループのときは何もしない
        if x == y:
            return False

        # union by size (y 側のサイズが小さくなるようにする)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # y を x の子とする
        self.par[y] = x
        # x のサイズを更新
        self.siz[x] += self.siz[y]

        return True

    def size(self, x: int) -> int:
        """
        x を含むグループのサイズを求める

        Args:
            x: 要素

        Returns:
            x を含むグループのサイズ
        """
        return self.siz[self.root(x)]
