"""
K番目に小さい積を二分探索で効率的に求める
時間計算量: O(N log N log C), 空間計算量: O(1)
"""

import bisect


def millionCellCalculation(arr1, arr2, K):
    arr1.sort()
    arr2.sort()

    # 積がターゲット以下の組み合わせが何通りあるかを二分探索で求める
    def count_less_equal(target):
        count = 0
        for a in arr1:
            if a * arr2[0] > target:
                break
            # arr2でa*bj <= targetとなる最大のインデックスを二分探索
            # 数学的変形によりtargetをaで除することでarr[j]が求まる
            # 数学的変形
            # - a * arr2[j] <= target
            # - arr2[j] <= target / a
            # - arr2[j] <= target // a (整数除算)
            right = bisect.bisect_right(arr2, target // a)
            count += right
        return count

    # 二分探索の範囲設定
    left = arr1[0] * arr2[0]
    right = arr1[-1] * arr2[-1]

    # K番目の値を二分探索
    while left < right:
        mid = (left + right) // 2
        # midよりKがまだ大きい場合には探索範囲を大きい方にシフト
        if count_less_equal(mid) < K:
            left = mid + 1
        else:
            right = mid

    return left
