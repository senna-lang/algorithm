"""
最大仲良しペア問題
AtCoder Regular Contest 092 C - 2D Plane 2N Points

問題:
- 2次元平面上に赤い点と青い点がN個ずつある
- 仲良しペア: 赤(rx, ry)と青(bx, by)で rx < bx かつ ry < by
- 最大で何個の仲良しペアを作れるかをO(N log N)で求める

貪欲法の戦略:
1. 赤い点をy座標で昇順ソート
2. 青い点をy座標で昇順ソート
3. 赤い点を順に処理し、条件を満たすx座標が最小の青い点を選ぶ
4. これにより、x座標が大きい青い点を後のために残せる

重要な観察:
- y座標でソートすることで、y座標の条件は自動的に満たされる
- 各赤い点に対して、使える青い点の中でx座標が最小のものを貪欲に選ぶ
"""


def maximum_friendly_pairs(red_points: list[tuple[int, int]],
                          blue_points: list[tuple[int, int]]) -> int:
    """
    最大仲良しペア数を計算する（貪欲法）

    アルゴリズム:
    1. 赤い点をy座標で昇順ソート
    2. 青い点をy座標で昇順ソート
    3. 各赤い点について、y座標条件を満たす青い点の中で
       x座標が最小のものを選ぶ

    Args:
        red_points: 赤い点のリスト [(x, y), ...]
        blue_points: 青い点のリスト [(x, y), ...]

    Returns:
        作成可能な最大ペア数
    """
    # 赤い点をy座標で昇順ソート（y座標が同じならx座標で昇順）
    red_sorted = sorted(red_points, key=lambda p: (p[1], p[0]))
    # 青い点をy座標で昇順ソート（y座標が同じならx座標で昇順）
    blue_sorted = sorted(blue_points, key=lambda p: (p[1], p[0]))

    pair_count = 0
    used = [False] * len(blue_sorted)

    # 赤い点を順に処理
    for rx, ry in red_sorted:
        best_idx = -1
        best_x = float('inf')

        # ry < by を満たす青い点を探す
        for i in range(len(blue_sorted)):
            if used[i]:
                continue

            bx, by = blue_sorted[i]

            # y座標がryより小さいまたは等しい場合はスキップ
            if by <= ry:
                continue

            # y座標条件を満たす青い点が見つかった
            # x座標条件も確認
            if rx < bx:
                # x座標が最小のものを選ぶ（貪欲選択）
                if bx < best_x:
                    best_x = bx
                    best_idx = i

        # マッチする青い点が見つかった場合
        if best_idx != -1:
            used[best_idx] = True
            pair_count += 1

    return pair_count


def main() -> None:
    """メイン処理"""
    # 入力
    N = int(input())
    red_points = []
    blue_points = []

    # 赤い点を入力
    for _ in range(N):
        x, y = map(int, input().split())
        red_points.append((x, y))

    # 青い点を入力
    for _ in range(N):
        x, y = map(int, input().split())
        blue_points.append((x, y))

    # 答え
    result = maximum_friendly_pairs(red_points, blue_points)
    print(result)


if __name__ == "__main__":
    main()
