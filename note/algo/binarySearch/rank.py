def rank(arr):
    n = len(arr)
    sortedArr = sorted(arr)
    ranks = [0] * n

    for i in range(n):
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            # midは次のループでは探索しなくていいのでmid±1をする
            if sortedArr[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1

        ranks[i] = left  # leftが最終的な位置

    return ranks


testArr = [12, 43, 7, 15, 9]
print(rank(testArr))
