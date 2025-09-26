def subsetSum1(arr, W):
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


def subsetSum2(arr, W):
    n = len(arr)
    # dp[i][j] = i番目までのアイテムを使って和jが作れるかどうか (True/False)
    dp = [[False] * (W + 1) for _ in range(n + 1)]

    # 和0は何も選ばないことで常に作れる
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(W + 1):
            # i番目のアイテムを選ばない場合
            dp[i][j] = dp[i - 1][j]

            # i番目のアイテムを選ぶ場合
            if j >= arr[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    # 1以上W以下で作れる和の個数を数える
    count = 0
    for j in range(1, W + 1):
        if dp[n][j]:
            count += 1

    return count


def subsetSum3(arr, k, W):
    n = len(arr)
    # dp[i][j][w] = i番目までの要素から j個選んで和wが作れるかどうか
    dp = [[[False for _ in range(W + 1)] for _ in range(k + 1)] for _ in range(n + 1)]

    # 初期化：0個選んで和0は常に可能
    for i in range(n + 1):
        dp[i][0][0] = True

    for i in range(1, n + 1):
        for j in range(k + 1):
            for w in range(W + 1):
                # i番目の要素を選ばない場合
                dp[i][j][w] = dp[i - 1][j][w]

                # i番目の要素を選ぶ場合
                if j > 0 and w >= arr[i - 1]:
                    dp[i][j][w] = dp[i][j][w] or dp[i - 1][j - 1][w - arr[i - 1]]

    # k個以下で和Wが作れるかチェック
    for j in range(k + 1):
        if dp[n][j][W]:
            return True
    return False


def unboundedSubsetSum(arr, W):
    n = len(arr)
    # dp[w] = 和wが作れるかどうか
    dp = [False] * (W + 1)
    dp[0] = True

    # 各アイテムについて
    for i in range(n):
        # そのアイテムを使って更新可能な全ての和を更新
        for w in range(arr[i], W + 1):
            if dp[w - arr[i]]:
                dp[w] = True

    return dp[W]


def boundedSubsetSum(arr, limits, W):
    n = len(arr)
    # dp[i][w] = i番目までのアイテムを使って和wが作れるかどうか
    dp = [[False] * (W + 1) for _ in range(n + 1)]
    dp[0][0] = True  # 何も使わずに和0は作れる

    for i in range(1, n + 1):
        for w in range(W + 1):
            # i番目のアイテムを使わない場合
            dp[i][w] = dp[i - 1][w]

            # i番目のアイテムを1回以上使う場合
            for k in range(1, limits[i - 1] + 1):
                if (
                    w >= k * arr[i - 1] and dp[i - 1][w - k * arr[i - 1]]
                ):  # アイテムiをk回使ってもw以下である（iをk回使える）かつiをk回使った場合のdpデーブル参照がTrueの場合
                    dp[i][w] = True
                    break  # kループは１つTrueならTrueのため切り上げ可能

    return dp[n][W]


def lcs(S, T):
    m, n = len(S), len(T)

    # dp[i][j] = S[0:i]とT[0:j]のLCSの長さ
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                # 文字が一致する場合
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 文字が一致しない場合
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def maxAverageSum(arr, M):
    N = len(arr)

    # 累積和を事前計算（区間和を高速に求めるため）
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    def range_sum(i, j):
        """区間[i, j)の和を返す"""
        return prefix_sum[j] - prefix_sum[i]

    def range_avg(i, j):
        """区間[i, j)の平均を返す"""
        return range_sum(i, j) / (j - i)

    # dp[i][m] = 最初のi個の要素をm個の区間に分けた時の平均値の総和の最大値
    # 初期値は負の無限大（実現不可能を表す）
    dp = [[-float("inf")] * (M + 1) for _ in range(N + 1)]

    # 初期条件：0個の要素を0個の区間に分ける場合の和は0
    dp[0][0] = 0

    for i in range(1, N + 1):
        # 最初のi個の要素を最大M区間で何区間まで分割できるか
        for m in range(1, min(i, M) + 1):
            # 最後の区間の開始位置をjとする
            # m-1 → iまでの区間を位置jで分割する
            # m-1とすることでj以前の区間を確保する（j以前の区間はm-1個の区間で分けられるためjが最後の区間となる）
            for j in range(m - 1, i):
                # jより前の要素をm-1の区間で分けたときのコストが計算されていれば現在のdpを更新可能
                if dp[j][m - 1] != -float("inf"):
                    # 区間[j, i)を最後の区間とする
                    avg = range_avg(j, i)
                    # jより前の要素をm-1個の区間に分けたときの計算済みの最大値にj-i区間の平均値を足す
                    dp[i][m] = max(dp[i][m], dp[j][m - 1] + avg)

    return dp[N][M]
