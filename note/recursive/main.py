from typing import List


# O(log n)
def GCD(m: int, n: int):
    if n == 0:
        return m
    return GCD(n, m % n)


# print(GCD(51, 15))

memo = {}


# 0(N)
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

recursiveSubsetSum_memo = {}


# 0(2^N)
def recursiveSubsetSum(arr: List[int], w: int, num: int):
    key = (w, num)
    if key in recursiveSubsetSum_memo:
        return recursiveSubsetSum_memo[key]

    if num == 0:
        if w == 0:
            return True
        else:
            return False

    if recursiveSubsetSum(arr, w, num - 1):
        recursiveSubsetSum_memo[key] = True
        return True
    if recursiveSubsetSum(arr, w - arr[len(arr) - 2], num - 1):
        recursiveSubsetSum_memo[key] = True
        return True

    recursiveSubsetSum_memo[key] = False
    return False


arr = [0, 1, 2]
# print(recursiveSubsetSum(arr, 4, len(arr)))

tribo_memo = {}


# O(N)
def tribo(num: int):
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1

    if num in tribo_memo:
        return tribo_memo[num]

    tribo_memo[num] = tribo(num - 1) + tribo(num - 2) + tribo(num - 3)

    return tribo_memo[num]


# print(tribo(6))
