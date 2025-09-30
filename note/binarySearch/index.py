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
def binary_search():
    left, right = 0, 0

    while right - left > 1: # 最終的には１つの要素になってright(1) - left(0) = 1 となるため
        mid = left + (right - left) // 2
        # 条件が真なら答えは左にあるため右を切り捨て
        # 偽なら答えは右にあるため左を切り捨て
        if P(mid):
            right = mid
        else:
            left = mid

    return right
