from typing import List


# O(log n)
def GCD(m: int, n: int):
    if n == 0:
        return m
    return GCD(n, m % n)


# print(GCD(51, 15))


memo = {}


def fibo(num: int):
    if num == 0:
        return 0
    if num == 1:
        return 1

    if num in memo:
        return memo[num]

    memo[num] = fibo(num - 1) + fibo(num - 2)

    return memo[num]


# print(fibo(6))

# 0(2^N)
def recursiveSubsetSum(arr: List[int], w: int, num: int):
    if num == 0:
        if w == 0:
            return True
        else:
            return False

    if recursiveSubsetSum(arr, w, num - 1):
        return True
    if recursiveSubsetSum(arr, w - arr[len(arr) - 2], num - 1):
        return True

    return False


arr = [0, 1, 2]
print(recursiveSubsetSum(arr, 1, len(arr)))
