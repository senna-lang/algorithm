# -*- coding: utf-8 -*-
"""
橋(Bridge)検出アルゴリズム

連結な無向グラフ G = (V, E) が与えられたとき、全ての橋を求める。
橋とは、その辺を取り除いたらグラフが連結でなくなるような辺のこと。

アルゴリズム: Union-Findベース
- 各辺について、その辺を除外した状態でUnion-Findを構築
- 辺の両端点が同じ連結成分に属さない場合、その辺は橋
- 時間計算量: O(|E|^2 * α(|V|)) (全ての辺をチェック)
- 空間計算量: O(|V|)
"""

import sys
sys.path.append('../structures')
from typing import List, Tuple
from structures.unionFind import UnionFind


def count_bridges(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    Union-Findを使って橋の本数を求める

    各辺について、その辺を除いた状態でグラフを構築し、
    辺の両端点が連結かどうかを判定する

    Args:
        n: 頂点数 (頂点は 0 から n-1 でラベル付けされている)
        edges: 辺のリスト [(u, v), ...]

    Returns:
        橋の本数
    """
    bridge_count = 0

    # 各辺について、その辺が橋かどうか判定
    for i, (u, v) in enumerate(edges):
        uf = UnionFind(n)

        # 辺iを除外してグラフを形成
        for j, (a, b) in enumerate(edges):
            if i != j:
                uf.unite(a, b)

        # 辺(u, v)を除外した状態でuとvが連結でなければ、この辺は橋
        # 同じ集合に属していないということはu, v以外で形成されたグラフで連結しなかったということ
        # つまり辺(u, v)だけがグラフを連結させる辺（橋）だったことになる
        if not uf.isSame(u, v):
            bridge_count += 1

    return bridge_count
