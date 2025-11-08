from structures.unionFind import UnionFind


def decayedBridge(N: int, edges: list[tuple[int, int]]):
    """
    各辺を崩壊させた際の連結成分数を求める（順方向アプローチ）

    時間計算量: O(|E|^2 * α(N))
    空間計算量: O(N)

    注意: このアプローチは動作するが効率が悪い
    """
    edgesN = len(edges)
    t = [0] * edgesN

    for i, (u, v) in enumerate(edges):
        uf = UnionFind(N)
        for j, (a, b) in enumerate(edges):
            if i != j:
                uf.unite(a, b)

        count = 0
        for x in range(N):
            if uf.root(x) == x:
                count += 1

        t[i] = count

    return t


# ============================================================
# 正解: 逆方向アプローチ（効率的な解法）
# ============================================================


def decayedBridge_optimal(N: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    各辺を崩壊させた際の連結成分数を求める（逆方向アプローチ）

    アルゴリズム:
    1. 最初は全頂点が孤立（連結成分数 = N）
    2. 辺を逆順に追加していく
    3. 各ステップで連結成分数を記録
    4. 最後に結果を反転

    時間計算量: O(|E| * α(N))
    空間計算量: O(N + |E|)
    """
    edgesN = len(edges)
    uf = UnionFind(N)

    # 初期状態: 全頂点が孤立
    component_count = N
    result = []

    # 辺を逆順に処理
    for i in range(edgesN - 1, -1, -1):
        # i番目の辺を崩壊させた後の連結成分数を記録
        result.append(component_count)

        # 辺を追加（時間を逆行）
        u, v = edges[i]
        if not uf.isSame(u, v):
            uf.unite(u, v)
            component_count -= 1  # 連結成分が1つ減る

    # 結果を反転して返す
    return result[::-1]
