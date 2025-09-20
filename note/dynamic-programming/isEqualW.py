def isEqualW(arr, W):
    """
    部分和問題をO(NW)で解く

    Args:
        arr: N個の正の整数のリスト
        W: 目標とする和

    Returns:
        bool: 和がWになる部分集合が存在するかどうか
    """
    N = len(arr)

    # dp[i][w] = 最初のi個の要素で和wが作れるかどうか
    dp = [[False] * (W + 1) for _ in range(N + 1)]

    # 初期条件：何も選ばなければ和は0
    for i in range(N + 1):
        dp[i][0] = True

    # DPテーブルの更新
    for i in range(1, N + 1):
        for w in range(W + 1):
            # i番目の要素を選ばない場合
            dp[i][w] = dp[i - 1][w]

            # i番目の要素を選ぶ場合（選べるなら）
            if w >= arr[i - 1]:
                dp[i][w] = dp[i][w] or dp[i - 1][w - arr[i - 1]]

    return dp[N][W]

# w=0  w=1  w=2  w=3  w=4  w=5  w=6  w=7
# i=0    T    F    F    F    F    F    F    F    (要素なし)
# i=1    T    F    F    T    F    F    F    F    (要素[3])
# i=2    T    F    F    T    T    F    F    T    (要素[3,4])
# i=3    T    F    F    T    T    T    F    T    (要素[3,4,5])