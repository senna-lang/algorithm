"""
重み付きUnion-Find (Weighted Union-Find) の実装

通常のUnion-Findに「重み」の概念を追加したデータ構造。
各要素から根までの重み（距離）を管理する。

用途:
- 相対的な位置関係を管理（x_i - x_j = d のような制約）
- グラフ上の距離管理
- ポテンシャル関数の管理

時間計算量: ほぼ O(1) (正確には O(α(N)))
空間計算量: O(N)
"""


class WeightedUnionFind:
    """
    重み付きUnion-Find

    各要素xについて、weight[x] = (xから根までの重み) を管理
    重みの意味: parent[x]からxへの重み（親から子への重み）

    Attributes:
        par: 親ノードの配列 (par[x] = -1 なら x が根)
        weight: 親からの重みの配列
    """

    def __init__(self, n: int) -> None:
        """
        重み付きUnion-Findを初期化

        Args:
            n: 要素数

        初期状態: 各要素が独立したグループ、重みは全て0
        """
        self.par = [-1] * n  # 親ノード (-1なら根)
        self.weight = [0] * n  # 親からの重み

    def root(self, x: int) -> int:
        """
        xの根を求める（経路圧縮あり）

        経路圧縮時に重みも更新する:
        - 元の親からの重みと、親の根までの重みを合計

        Args:
            x: 要素

        Returns:
            xの属するグループの根
        """
        if self.par[x] == -1:
            return x

        # 経路圧縮: 親を根に更新
        r = self.root(self.par[x])
        # 重みを更新: 元の親からの重み + 親の根までの重み
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = r
        return r

    def get_weight(self, x: int) -> int:
        """
        xから根までの重みを取得

        Args:
            x: 要素

        Returns:
            xから根までの累積重み
        """
        self.root(x)  # 経路圧縮して重みを更新
        return self.weight[x]

    def diff(self, x: int, y: int) -> int:
        """
        yからxへの重み（x - y）を計算

        Args:
            x: 要素1
            y: 要素2

        Returns:
            x - y の重み

        注意: xとyが同じグループに属していない場合は不正確
        """
        return self.get_weight(x) - self.get_weight(y)

    def isSame(self, x: int, y: int) -> bool:
        """
        xとyが同じグループに属するか判定

        Args:
            x: 要素1
            y: 要素2

        Returns:
            同じグループならTrue
        """
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int, w: int) -> bool:
        """
        「y - x = w」という制約を追加してグループを併合

        つまり、weight[y] - weight[x] = w となるように併合

        Args:
            x: 要素1
            y: 要素2
            w: yからxへの重み (y - x = w)

        Returns:
            併合が行われた場合True、既に同じグループの場合False

        注意:
        既に同じグループの場合、制約が矛盾していないか確認が必要
        （このメソッド内では確認しない）
        """
        # 各要素の根までの重みを取得
        weight_x = self.get_weight(x)
        weight_y = self.get_weight(y)

        # 根を取得
        root_x = self.root(x)
        root_y = self.root(y)

        # 既に同じグループ
        if root_x == root_y:
            return False

        # root_yをroot_xの子にする
        self.par[root_y] = root_x

        # root_yの重みを設定
        # 目標: weight[y] - weight[x] = w
        # weight[y] = weight_y + weight[root_y]
        # weight[x] = weight_x
        # よって: (weight_y + weight[root_y]) - weight_x = w
        # weight[root_y] = w - weight_y + weight_x
        self.weight[root_y] = w - weight_y + weight_x

        return True

    def is_valid_constraint(self, x: int, y: int, w: int) -> bool:
        """
        「y - x = w」という制約が現在の状態と矛盾しないか確認

        Args:
            x: 要素1
            y: 要素2
            w: yからxへの重み (y - x = w)

        Returns:
            制約が矛盾しない場合True、矛盾する場合False
        """
        if not self.isSame(x, y):
            return True  # 異なるグループなら矛盾しない（併合可能）

        # 同じグループの場合、既存の重み関係と一致するかチェック
        return self.diff(y, x) == w
