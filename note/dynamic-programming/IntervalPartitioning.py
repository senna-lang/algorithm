INF = 1 << 60  # 2^60


def intervalPartitioning():
    # 入力
    N = int(input())
    c = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(N + 1):
            c[i][j] = int(input())

    # DPテーブル定義
    dp = [INF] * (N + 1)

    # DP初期条件
    dp[0] = 0

    # DPループ
    for rp in range(N + 1):
        for lp in range(rp):  # rpを起点にlpの位置を１ずつづらす
            dp[rp] = min(
                dp[rp], dp[lp] + c[lp][rp]
            )  # rpを起点にどこをlpにすると一番コストが低いかを緩和で求める

    # dpの最後の要素が配列の終端での最小コストとなる
    print(dp[N])
