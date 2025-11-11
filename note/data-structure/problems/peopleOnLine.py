"""
問題11.4: People on a Line (数直線上の人々)

M組の整数ペア (l_i, r_i, d_i) が与えられる。
各ペアについて x_{r_i} - x_{l_i} = d_i を満たす
N個の整数 x_0, x_1, ..., x_{N-1} が存在するかどうかを判定する。

出典: AtCoder Regular Contest 090 D - People on a Line
"""

from structures.weightedUnionFind import WeightedUnionFind


def can_construct_line(N: int, constraints: list[tuple[int, int, int]]) -> bool:
    """
    制約を満たす数列が構築可能か判定

    問題の本質:
    - 複数の制約 x_r - x_l = d が与えられる
    - これらの制約が矛盾せずに全て満たせるかを判定
    - 例: x_1 - x_0 = 3, x_2 - x_1 = 4 なら x_2 - x_0 = 7 が自動的に決まる
    - もし x_2 - x_0 = 6 という制約が来たら矛盾（7 ≠ 6）

    アルゴリズム:
    1. 重み付きUnion-Findで各要素間の相対的な位置関係を管理
    2. 新しい制約が来たら:
       - 既に関係が確定している場合 → 矛盾チェック
       - まだ関係が未確定の場合 → 制約を追加（グループを併合）
    3. 全ての制約を矛盾なく追加できればTrue

    Args:
        N: 要素数（x_0, x_1, ..., x_{N-1}）
        constraints: [(l, r, d), ...] のリスト
                     各要素は「x_r - x_l = d」を表す

    Returns:
        全ての制約を満たす数列が存在する場合True、矛盾がある場合False

    時間計算量: O(M * α(N))  M = 制約の数
    空間計算量: O(N)
    """
    # 重み付きUnion-Findを初期化
    # 各要素 x_i を管理し、要素間の差（重み）を記録する
    uf = WeightedUnionFind(N)

    # 全ての制約を順番に処理
    for l, r, d in constraints:
        # 現在の制約: x_r - x_l = d
        # 例: l=0, r=2, d=5 → x_2 - x_0 = 5

        # ケース1: lとrが既に同じグループに属している
        # → 過去の制約から x_r - x_l の関係が既に確定している
        if uf.isSame(l, r):
            # 既存の重み関係（x_r - x_l の値）を取得
            existing_diff = uf.diff(r, l)

            # 新しい制約の値dと既存の値が一致するかチェック
            if existing_diff != d:
                # 矛盾を検出！
                # 例: 既に x_2 - x_0 = 7 と確定しているのに
                #     x_2 - x_0 = 6 という制約が来た場合
                return False

        # ケース2: lとrがまだ異なるグループ
        # → この制約によって初めて関係が確定する
        else:
            # x_r - x_l = d という関係を登録し、グループを併合
            # これにより、以降はこの2つの要素の差が確定する
            uf.unite(l, r, d)

    # 全ての制約を矛盾なく処理できた
    # → 制約を満たす数列が存在する
    return True
