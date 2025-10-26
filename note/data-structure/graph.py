"""
グラフの表現と入力処理

Code 10.2, 10.3: グラフを隣接リストとして入力・構築する

グラフの表現方法:
1. 隣接リスト (Adjacency List): Graph = list[list[int]]
   - Graph[v] = 頂点 v に隣接する頂点のリスト
   - メモリ効率が良い: O(V + E)
   - 辺の列挙が高速: O(次数)

2. 隣接行列 (Adjacency Matrix): Graph = list[list[bool]]
   - Graph[u][v] = 辺 (u, v) が存在するか
   - 辺の存在確認が高速: O(1)
   - メモリ使用量が大きい: O(V^2)

入力形式 (Code 10.2):
- 1行目: N (頂点数), M (辺数)
- 2行目以降: a, b (辺 a→b)

時間計算量: O(M) (辺の数だけループ)
空間計算量: O(N + M) (隣接リスト)
"""

from typing import Optional, NamedTuple

# グラフの型定義

# 1. 重みなしグラフ (Unweighted Graph)
# Graph = 隣接リストの二次元配列
# Graph[v] = 頂点 v から出ている辺の隣接頂点リスト
Graph = list[list[int]]


# 2. 重み付きグラフ (Weighted Graph)
class Edge(NamedTuple):
    """
    重み付き辺を表すクラス

    Attributes:
        to: 行き先の頂点
        weight: 辺の重み
    """
    to: int
    weight: int  # または float


# WeightedGraph = 重み付き隣接リスト
# WeightedGraph[v] = 頂点 v から出ている辺のリスト
WeightedGraph = list[list[Edge]]


def read_graph_from_input() -> tuple[int, int, Graph]:
    """
    標準入力からグラフを読み込む (有向グラフ)

    入力形式:
        N M
        a1 b1
        a2 b2
        ...
        aM bM

    Returns:
        タプル (N, M, G)
        - N: 頂点数
        - M: 辺数
        - G: グラフの隣接リスト

    Examples:
        入力:
        8 13
        4 1
        4 2
        ...

        出力:
        (8, 13, [[...], [...], ...])
    """
    # 頂点数と辺数
    N, M = map(int, input().split())

    # グラフ (隣接リスト)
    G: Graph = [[] for _ in range(N)]

    # 辺の読み込み
    for _ in range(M):
        a, b = map(int, input().split())
        #  辺の始点であるaを起点となる頂点としてG[a]に終点（隣接した頂点）をappendする
        G[a].append(b)

    return N, M, G


def read_graph_from_list(
    N: int, edges: list[tuple[int, int]], directed: bool = True
) -> Graph:
    """
    辺のリストからグラフを構築する

    Args:
        N: 頂点数
        edges: 辺のリスト [(a, b), ...]
        directed: 有向グラフかどうか (デフォルト: True)

    Returns:
        グラフの隣接リスト

    Examples:
        >>> edges = [(4, 1), (4, 2), (4, 6)]
        >>> G = read_graph_from_list(8, edges)
        >>> G[4]
        [1, 2, 6]
    """
    G: Graph = [[] for _ in range(N)]

    for a, b in edges:
        G[a].append(b)

        # 無向グラフの場合は逆辺も追加
        if not directed:
            G[b].append(a)

    return G


def read_undirected_graph_from_list(N: int, edges: list[tuple[int, int]]) -> Graph:
    """
    無向グラフを辺のリストから構築する

    Args:
        N: 頂点数
        edges: 辺のリスト [(a, b), ...]

    Returns:
        グラフの隣接リスト (無向グラフ)

    Examples:
        >>> edges = [(0, 1), (1, 2)]
        >>> G = read_undirected_graph_from_list(3, edges)
        >>> G[0]
        [1]
        >>> G[1]
        [0, 2]
    """
    return read_graph_from_list(N, edges, directed=False)


def visualize_graph(G: Graph, node_labels: Optional[list[str]] = None) -> str:
    """
    グラフを視覚的に表示する

    Args:
        G: グラフの隣接リスト
        node_labels: 各ノードのラベル (省略時は数値)

    Returns:
        グラフの文字列表現
    """
    lines = []
    lines.append("=== グラフの隣接リスト ===")

    N = len(G)
    for v in range(N):
        label = node_labels[v] if node_labels else str(v)
        neighbors = ", ".join(str(node_labels[u] if node_labels else u) for u in G[v])
        lines.append(f"  {label}: [{neighbors}]")

    return "\n".join(lines)


def count_edges(G: Graph, directed: bool = True) -> int:
    """
    グラフの辺数を数える

    Args:
        G: グラフの隣接リスト
        directed: 有向グラフかどうか

    Returns:
        辺の数
    """
    total = sum(len(neighbors) for neighbors in G)

    if not directed:
        # 無向グラフの場合は2で割る (各辺が2回カウントされるため)
        total //= 2

    return total


def get_out_degree(G: Graph, v: int) -> int:
    """
    頂点の出次数を取得する

    Args:
        G: グラフの隣接リスト
        v: 頂点

    Returns:
        頂点 v の出次数 (隣接する頂点の数)
    """
    return len(G[v])


def get_in_degree(G: Graph, v: int) -> int:
    """
    有向グラフにおける頂点の入次数を取得する

    Args:
        G: グラフの隣接リスト
        v: 頂点

    Returns:
        頂点 v への入ってくる辺の数
    """
    count = 0
    for neighbors in G:
        if v in neighbors:
            count += 1
    return count


def has_edge(G: Graph, u: int, v: int) -> bool:
    """
    辺 (u, v) が存在するかチェック

    Args:
        G: グラフの隣接リスト
        u: 始点
        v: 終点

    Returns:
        辺 (u, v) が存在するか
    """
    return v in G[u]


# ===== 重み付きグラフ用の関数 =====


def read_weighted_graph_from_input() -> tuple[int, int, WeightedGraph]:
    """
    標準入力から重み付きグラフを読み込む (有向グラフ)

    入力形式:
        N M
        a1 b1 w1
        a2 b2 w2
        ...
        aM bM wM

    Returns:
        タプル (N, M, G)
        - N: 頂点数
        - M: 辺数
        - G: 重み付きグラフの隣接リスト

    Examples:
        入力:
        4 5
        0 1 2
        0 2 3
        1 2 1
        1 3 4
        2 3 2

        出力:
        (4, 5, [[Edge(to=1, weight=2), Edge(to=2, weight=3)], ...])
    """
    # 頂点数と辺数
    N, M = map(int, input().split())

    # グラフ (隣接リスト)
    G: WeightedGraph = [[] for _ in range(N)]

    # 辺の読み込み
    for _ in range(M):
        a, b, w = map(int, input().split())
        G[a].append(Edge(to=b, weight=w))

    return N, M, G


def read_weighted_graph_from_list(
    N: int, edges: list[tuple[int, int, int]], directed: bool = True
) -> WeightedGraph:
    """
    辺のリストから重み付きグラフを構築する

    Args:
        N: 頂点数
        edges: 辺のリスト [(a, b, w), ...] (a→b、重みw)
        directed: 有向グラフかどうか (デフォルト: True)

    Returns:
        重み付きグラフの隣接リスト

    Examples:
        >>> edges = [(0, 1, 2), (0, 2, 3), (1, 3, 4)]
        >>> G = read_weighted_graph_from_list(4, edges)
        >>> G[0]
        [Edge(to=1, weight=2), Edge(to=2, weight=3)]
    """
    G: WeightedGraph = [[] for _ in range(N)]

    for a, b, w in edges:
        G[a].append(Edge(to=b, weight=w))

        # 無向グラフの場合は逆辺も追加
        if not directed:
            G[b].append(Edge(to=a, weight=w))

    return G


def visualize_weighted_graph(
    G: WeightedGraph, node_labels: Optional[list[str]] = None
) -> str:
    """
    重み付きグラフを視覚的に表示する

    Args:
        G: 重み付きグラフの隣接リスト
        node_labels: 各ノードのラベル (省略時は数値)

    Returns:
        グラフの文字列表現
    """
    lines = []
    lines.append("=== 重み付きグラフの隣接リスト ===")

    N = len(G)
    for v in range(N):
        label = node_labels[v] if node_labels else str(v)
        edges_str = ", ".join(
            f"{node_labels[e.to] if node_labels else e.to}({e.weight})"
            for e in G[v]
        )
        lines.append(f"  {label}: [{edges_str}]")

    return "\n".join(lines)


def has_weighted_edge(G: WeightedGraph, u: int, v: int) -> Optional[int]:
    """
    辺 (u, v) が存在するかチェックし、存在する場合は重みを返す

    Args:
        G: 重み付きグラフの隣接リスト
        u: 始点
        v: 終点

    Returns:
        辺が存在する場合はその重み、存在しない場合は None
    """
    for edge in G[u]:
        if edge.to == v:
            return edge.weight
    return None


def main() -> None:
    """使用例とテストケース"""
    print("=== グラフの入力と構築 ===\n")

    # Code 10.2 の入力例
    print("Code 10.2 の入力例:")
    edges_example = [
        (4, 1),
        (4, 2),
        (4, 6),
        (1, 3),
        (1, 6),
        (2, 5),
        (2, 7),
        (6, 7),
        (3, 0),
        (3, 7),
        (7, 0),
        (0, 5),
    ]

    N = 8
    M = len(edges_example)
    G = read_graph_from_list(N, edges_example, directed=True)

    print(f"頂点数: {N}")
    print(f"辺数: {M}")
    print()
    print(visualize_graph(G))
    print()

    # 各頂点の次数を表示
    print("=== 各頂点の出次数 ===")
    for v in range(N):
        out_deg = get_out_degree(G, v)
        in_deg = get_in_degree(G, v)
        print(f"  頂点 {v}: 出次数 = {out_deg}, 入次数 = {in_deg}")
    print()

    # 辺の存在確認
    print("=== 辺の存在確認 ===")
    test_edges = [(4, 1), (4, 3), (0, 5), (5, 0)]
    for u, v in test_edges:
        exists = has_edge(G, u, v)
        print(f"  辺 ({u}, {v}): {'存在する' if exists else '存在しない'}")
    print()

    # 無向グラフの例
    print("=== 無向グラフの例 ===")
    edges_undirected = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    G_undirected = read_undirected_graph_from_list(4, edges_undirected)

    print("頂点数: 4")
    print(f"辺数: {len(edges_undirected)}")
    print()
    print(visualize_graph(G_undirected))
    print()

    # 無向グラフの次数
    print("=== 各頂点の次数（無向グラフ） ===")
    for v in range(len(G_undirected)):
        deg = get_out_degree(G_undirected, v)
        print(f"  頂点 {v}: 次数 = {deg}")
    print()

    # 重み付きグラフの例
    print("=== 重み付きグラフの例 ===")
    weighted_edges = [
        (0, 1, 2),   # 0→1、重み2
        (0, 2, 3),   # 0→2、重み3
        (1, 2, 1),   # 1→2、重み1
        (1, 3, 4),   # 1→3、重み4
        (2, 3, 2),   # 2→3、重み2
    ]
    G_weighted = read_weighted_graph_from_list(4, weighted_edges, directed=True)

    print("頂点数: 4")
    print(f"辺数: {len(weighted_edges)}")
    print()
    print(visualize_weighted_graph(G_weighted))
    print()

    # 重み付き辺の存在確認
    print("=== 重み付き辺の存在確認 ===")
    test_weighted_edges = [(0, 1), (0, 3), (1, 3), (2, 3)]
    for u, v in test_weighted_edges:
        weight = has_weighted_edge(G_weighted, u, v)
        if weight is not None:
            print(f"  辺 ({u}, {v}): 存在する（重み = {weight}）")
        else:
            print(f"  辺 ({u}, {v}): 存在しない")
    print()

    # 無向重み付きグラフの例
    print("=== 無向重み付きグラフの例 ===")
    undirected_weighted_edges = [
        (0, 1, 5),
        (1, 2, 3),
        (2, 3, 7),
        (3, 0, 2),
    ]
    G_undirected_weighted = read_weighted_graph_from_list(
        4, undirected_weighted_edges, directed=False
    )

    print("頂点数: 4")
    print(f"辺数: {len(undirected_weighted_edges)}")
    print()
    print(visualize_weighted_graph(G_undirected_weighted))


if __name__ == "__main__":
    main()
