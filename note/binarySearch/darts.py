import bisect


def max_sum_of_four(a, M):
    n = len(a)

    # 2個の和を全て列挙 O(N^2)
    pair_sums = []
    for i in range(n):
        for j in range(n):  # 重複を許すので i から n まで
            pair_sums.append(a[i] + a[j])

    # ソート O(N^2 log N^2) = O(N^2 log N)
    pair_sums.sort()

    max_value = -1  # 見つからない場合は -1 など

    # 各ペアの和について O(N^2)
    for s1 in pair_sums:
        if s1 > M:
            break

        # s1 + s2 <= M となる最大の s2 を二分探索 O(log N^2) = O(log N)
        target = M - s1

        # target 以下の最大値を探す
        # bisect_right(pair_sums, target) - 1 が target 以下の最後の位置
        pos = bisect.bisect_right(pair_sums, target) - 1

        if pos >= 0:
            s2 = pair_sums[pos]
            max_value = max(max_value, s1 + s2)

    return max_value


# テスト
a = [1, 2, 3, 4]
M = 10

result = max_sum_of_four(a, M)
print(f"最大値: {result}")

# 例: 4+4+1+1=10, 4+3+2+1=10 など
