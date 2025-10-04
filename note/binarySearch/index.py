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