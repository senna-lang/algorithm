def knapsack():
    # テスト用の入力データを直接指定（最初の要素をNとWとする）
    test_data = ["3 8", "4 5", "5 6", "6 4"]

    # 最初の行から N, W を取得
    N, W = map(int, test_data[0].split())
    weight = []
    value = []

    # 各品物の重さと価値を取得
    for i in range(1, N + 1):
        w, v = map(int, test_data[i].split())
        weight.append(w)
        value.append(v)

    # DPテーブル定義
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # DPループ
    for i in range(
        N
    ):  # テーブルのi軸を網羅的に探索（i = 0 は全て0なのでdp[i + 1]で更新してくためN + 1は不要）
        for w in range(W + 1):  # テーブルのw軸を網羅的に探索
            # 品物を選ばない場合
            dp[i + 1][w] = dp[i][w]

        # 品物を選ぶ場合（選ばない場合の値がすでに更新済みなのでそれと選んだ場合を比較する）
        if (
            w >= weight[i]
        ):  # まず最大重量に対してi番目の対象物の重さが許容するかだけを考える
            dp[i + 1][w] = max(
                dp[i + 1][w], dp[i][w - weight[i]] + value[i]
            )  # 許容する場合対象物を入れた時の残りの許容重量での最大値に今回の対象物のvalueを追加する

    # 完成した最大値テーブルに対して入力
    print(dp[N][W])


knapsack()
