"""
区間スケジューリング問題に対する貪欲法
"""

from typing import List, Tuple


def solve_interval_scheduling(intervals: List[Tuple[int, int]]) -> int:
    """
    区間スケジューリング問題を貪欲法で解く

    Args:
        intervals: (開始時刻, 終了時刻) のタプルのリスト

    Returns:
        選択できる最大の区間数
    """
    if not intervals:
        return 0

    # 終了時刻が早い順にソート
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    # 貪欲に選ぶ
    res = 0
    current_end_time = 0

    for start, end in sorted_intervals:
        # 最後に選んだ区間と被るのは除く
        if start < current_end_time:
            continue

        res += 1
        current_end_time = end

    return res


def main():
    """メイン関数: 標準入力から区間を読み込み、結果を出力"""
    # 入力
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))

    # 解く
    result = solve_interval_scheduling(intervals)

    # 出力
    print(result)


if __name__ == "__main__":
    main()
