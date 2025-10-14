import bisect


def countTriples(a, b, c):
    n = len(a)

    # aとcをソート O(N log N)
    sorted_a = sorted(a)
    sorted_c = sorted(c)

    total = 0

    # 各b[j]について O(N log N)
    for j in range(n):
        # b[j]より小さいa[i]の個数
        # bisect_left(sorted_a, b[j]) = b[j]未満の要素数
        count_a = bisect.bisect_left(sorted_a, b[j])

        # b[j]より大きいc[k]の個数
        # n - bisect_right(sorted_c, b[j]) = b[j]より大きい要素数
        count_c = n - bisect.bisect_right(sorted_c, b[j])

        # この b[j] を中心とした組み合わせの数
        total += count_a * count_c

    return total


# テスト
a = [1, 5]
b = [2, 4]
c = [3, 6]

result = countTriples(a, b, c)
print(result)
