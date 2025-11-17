import bisect

INF = 20000000  # 十分大きな値


def binarySearch(arr, key):
    n = len(arr)

    left = 0
    right = n - 1

    while right >= left:
        mid = left + (right - left) / 2

        if mid == key:
            return mid
        elif mid >= key:
            right = mid - 1
        elif mid <= key:
            left = mid + 1
    return


# x が条件を満たすかどうか
def P(x):
    # ここに条件を実装
    pass


# P(x) = True となる最小の整数 x を返す
def binarySearch2():
    left, right = 0, 0

    while (
        right - left > 1
    ):  # 最終的には１つの要素になってright(1) - left(0) = 1 となるため
        mid = left + (right - left) // 2
        # 条件が真なら答えは左にあるため右を切り捨て
        # 偽なら答えは右にあるため左を切り捨て
        if P(mid):
            right = mid
        else:
            left = mid

    return right


def bisectBinarySearch():
    # 入力を受け取る
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 暫定最小値を格納する変数
    min_value = INF

    # b をソート
    b.sort()

    # a を固定して解く
    for i in range(N):
        # b の中で K - a[i] 以上の範囲での最小値を示すインデックス
        pos = bisect.bisect_left(b, K - a[i])

        # インデックスが範囲内かチェック
        if pos < N:
            val = b[pos]

            # min_value と比較する
            if a[i] + val < min_value:
                min_value = a[i] + val

    print(min_value)


def shootingKing():
    # 入力
    N = int(input())
    h = []  # 各風船の初期高度
    s = []  # 各風船の膨張速度
    for i in range(N):
        hi, si = map(int, input().split())
        h.append(hi)
        s.append(si)

    # 二分探索
    left = 0
    right = INF
    while right - left > 1:
        mid = (left + right) // 2  # midは高度として扱う

        # 判定
        ok = True
        t = [0] * N  # 各風船を割るまでの時間制限
        for i in range(N):
            # そもそも mid が初期高度より低かったら false
            if mid < h[i]:
                ok = False
            else:
                # 風船iは時刻tに高度h[i] + s[i] * tになる
                # 高度midに達する時刻は：h[i] + s[i] * t = mid
                # 解くと：t = (mid - h[i]) / s[i]
                # つまり、時刻t[i]までに風船iを割らないと手遅れになる
                t[i] = (mid - h[i]) // s[i]

        # 時間制限がきつい順にソート
        t.sort()
        for i in range(N):
            if t[i] < i: # 制限時間がきつい順番に１秒ごとに打っていった場合に最後まで制限時間内に収まっているか
                ok = False  # 時間切れ発生

        if ok: # 最後まで時間ないに収まる場合はもっと低い高度（難しい条件）に挑戦する
            right = mid
        else: # 制限時間をオーバーした場合は高い高度に条件を緩くする
            left = mid

    print(right)
