from typing import List


def min_cost_frog_jump_push(heights: List[int]):
    n = len(heights)
    if n <= 1:
        return 0

    # dp[i] = i番目の足場に到達するための最小コスト
    dp = [float("inf")] * n
    dp[0] = 0  # 最初の足場にいるのでコストは0

    for i in range(n):
        # 現在の足場から1つ先に移動
        if i + 1 < n:
            cost = abs(heights[i] - heights[i + 1])
            dp[i + 1] = min(dp[i + 1], dp[i] + cost)

        # 現在の足場から2つ先に移動
        if i + 2 < n:
            cost = abs(heights[i] - heights[i + 2])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost)

    return dp[n - 1]


def min_cost_frog_jump_pull(heights: List[int]):
    n = len(heights)
    if n <= 1:
        return 0

    # dp[i] = i番目の足場に到達するための最小コスト
    dp = [float("inf")] * n
    dp[0] = 0  # 最初の足場にいるのでコストは0

    for i in range(1, n):
        # 1つ前の足場から来る場合
        if i - 1 >= 0:
            cost = abs(heights[i] - heights[i - 1])
            dp[i] = min(dp[i], dp[i - 1] + cost)

        # 2つ前の足場から来る場合
        if i - 2 >= 0:
            cost = abs(heights[i] - heights[i - 2])
            dp[i] = min(dp[i], dp[i - 2] + cost)

    return dp[n - 1]
