"""
Aggressive Cows 問題のソリューション
N個の小屋からM個を選んで牛を配置し、選んだ牛同士の最小距離を最大化する
バイナリサーチを使用してO(N log A)で解く
"""

from typing import List


def can_place_cows(positions: List[int], min_distance: int, cows: int) -> bool:
    """
    指定された最小距離でcows匹の牛を配置できるかを判定

    Args:
        positions: ソート済みの小屋の座標リスト
        min_distance: 牛同士の最小距離
        cows: 配置する牛の数

    Returns:
        配置可能ならTrue、不可能ならFalse
    """
    if not positions or cows <= 0:
        return False

    count = 1  # 最初の位置に必ず1匹配置
    last_position = positions[0]

    for i in range(1, len(positions)):
        # 最小距離以上の間隔で何頭配置できるか
        if positions[i] - last_position >= min_distance:
            count += 1
            last_position = positions[i]
            if count >= cows:
                return True

    return count >= cows


def aggressive_cows(positions: List[int], cows: int) -> int:
    """
    M個の牛を配置して、選んだ牛同士の最小距離の最大値を求める

    Args:
        positions: 小屋の座標リスト (0 <= positions[i] <= A)
        cows: 配置する牛の数 (M <= N)

    Returns:
        選んだ牛同士の最小距離の最大値
    """
    if not positions or cows <= 0 or cows > len(positions):
        return 0

    # 座標をソート
    sorted_positions = sorted(positions)

    # バイナリサーチの範囲設定
    left = 0  # 最小距離の下限
    right = (
        sorted_positions[-1] - sorted_positions[0]
    )  # 最小距離の上限（最初の小屋と最後の小屋に配置した場合）
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place_cows(sorted_positions, mid, cows):
            result = mid  # 実現可能な距離を記録
            left = mid + 1  # より大きな距離を試す
        else:
            right = mid - 1  # より小さな距離を試す

    return result


# 使用例とテスト用の関数
def solve_aggressive_cows(n: int, m: int, positions: List[int]) -> int:
    """
    問題の入力形式に合わせたラッパー関数

    Args:
        n: 小屋の数
        m: 牛の数
        positions: 小屋の座標リスト

    Returns:
        選んだ牛同士の最小距離の最大値
    """
    return aggressive_cows(positions, m)
