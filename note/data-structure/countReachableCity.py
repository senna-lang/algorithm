from collections import defaultdict

from unionFind import UnionFind


def countReachableCity(
    N: int, kEdges: list[tuple[int, int]], lEdges: list[tuple[int, int]]
) -> list[int]:
    """
    道路と鉄道の両方で到達可能な都市数を求める（基本版）

    各都市について、道路のみでも鉄道のみでも到達できる都市数をカウント

    時間計算量: O(N^2 * α(N))
    空間計算量: O(N)

    注意: 正しく動作するが、N^2 の全ペアチェックが必要
    """
    kUf = UnionFind(N)
    lUf = UnionFind(N)

    for u, v in kEdges:
        if not kUf.isSame(u, v):
            kUf.unite(u, v)

    for u, v in lEdges:
        if not lUf.isSame(u, v):
            lUf.unite(u, v)

    reachableCity = [0] * N

    for i in range(N):
        for j in range(N):
            if kUf.isSame(i, j) and lUf.isSame(i, j):
                reachableCity[i] += 1

    return reachableCity


# ============================================================
# 最適化版
# ============================================================


def countReachableCity_optimal(
    N: int, kEdges: list[tuple[int, int]], lEdges: list[tuple[int, int]]
) -> list[int]:
    """
    道路と鉄道の両方で到達可能な都市数を求める（最適化版）

    アルゴリズム:
    1. 各都市が属する(道路の連結成分, 鉄道の連結成分)のペアを特定
    2. 同じペアに属する都市数をハッシュマップでカウント
    3. 各都市について、そのペアの出現回数を返す

    核心的なアイデア:
    - 都市iと都市jが両方で到達可能 ⟺ (kRoot[i], lRoot[i]) == (kRoot[j], lRoot[j])
    - 全ペアをチェックする代わりに、ペアごとに都市数を集計

    時間計算量: O((K + L + N) * α(N))
    空間計算量: O(N)
    """
    kUf = UnionFind(N)
    lUf = UnionFind(N)

    # 道路のグラフを構築
    for u, v in kEdges:
        kUf.unite(u, v)

    # 鉄道のグラフを構築
    for u, v in lEdges:
        lUf.unite(u, v)

    # 各(kRoot, lRoot)ペアの出現回数をカウント
    pair_count = defaultdict(int)

    for i in range(N):
        k_root = kUf.root(i)
        l_root = lUf.root(i)
        pair_count[(k_root, l_root)] += 1

    # 各都市について、同じペアに属する都市数を取得
    # 同じペアを持つということは「同じ道路集合かつ同じ鉄道集合に属する」＝車でも電車でも到達可能な関係性
    result = []
    for i in range(N):
        k_root = kUf.root(i)
        l_root = lUf.root(i)
        result.append(pair_count[(k_root, l_root)])

    return result
