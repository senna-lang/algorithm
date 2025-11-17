def edit_distance(s, t):
    """
    編集距離を動的計画法を用いて求める

    Args:
        s (str): 文字列1
        t (str): 文字列2

    Returns:
        int: 編集距離
    """
    # 文字列の長さ
    s_len = len(s)
    t_len = len(t)

    # 十分大きな値（無限大の代わり）
    INF = float("inf")

    # DPテーブル定義
    # dp[i][j] = s[0:i]とt[0:j]の編集距離
    dp = [[INF for _ in range(t_len + 1)] for _ in range(s_len + 1)]

    # DP初期条件
    dp[0][0] = 0

    # DPループ
    for i in range(s_len + 1):
        for j in range(t_len + 1):
            # 変更経路
            if i > 0 and j > 0:
                if s[i - 1] == t[j - 1]:
                    # 文字が同じ場合は変更不要
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    # 文字が異なる場合は変更コスト+1
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            # 削除経路
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

            # 挿入経路
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    return dp[s_len][t_len]


edit_distance("test", "anstq")
