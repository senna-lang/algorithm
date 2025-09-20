def summerVacation(N: int):
    import random

    c = [[random.randint(1, 100) for _ in range(3)] for _ in range(N)]

    # dp[i][j] = i日目に活動jを選んだときの最大幸福度
    dp = [[0] * 3 for _ in range(N)]

    # 初期化：0日目
    for j in range(3):
        dp[0][j] = c[0][j]

    # DPの更新
    for i in range(1, N):
        for j in range(3):  # 今日の活動
            for k in range(3):  # 前日の活動
                if j != k:  # 連続して同じ活動をしない
                    dp[i][j] = max(
                        dp[i][j], dp[i - 1][k] + c[i][j]
                    )  # 今日の活動３種（j）それぞれを昨日の活動３種（k）と足し合わせmaxで最大値を求める

    # 最後の日の最大値を返す
    return max(dp[N - 1])
