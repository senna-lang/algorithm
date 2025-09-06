from typing import List

numArr = [1, 2, 3, 4, 5]
numArrAr1 = [1, 2, 3, 4, 5]
numArrAr2 = [6, 7, 8, 9, 10]


# O(N)
def linearSearch(numArr: List[int], num: int) -> bool:
    for i in range(len(numArr)):
        if numArr[i] == num:
            return True

    return False


# print(linearSearch(numArr,1))


def linearSearchFindIndex(numArr: List[int], num: int) -> int | bool:
    foundIndex = -1
    for i in range(len(numArr)):
        if numArr[i] == num:
            foundIndex = i
            return foundIndex

    return False


# print(linearSearchFindIndex(numArr, 9))


def linearSearchFindMinNum(numArr: List[int]) -> int:
    minNum = numArr[0]
    for i in range(1, len(numArr)):
        if numArr[i] < minNum:
            minNum = numArr[i]

    return minNum


# print(linearSearchFindMinNum(numArr))


def linearSearchFindMinTotal(numArr1: List[int], numArr2: List[int]) -> int:
    minTotal = numArr1[0] + numArr2[0]
    for i in range(len(numArr1)):
        for j in range(len(numArr2)):
            total = numArr1[i] + numArr2[j]
            if total < minTotal:
                minTotal = total

    return minTotal


# print(linearSearchFindMinTotal(numArrAr1, numArrAr2))


def subsetSum(nums: List[int], target: int) -> bool:
    n = len(nums)
    for bit in range(1 << n):  # 2^n通りの部分集合のパターンを列挙
        subset_sum = 0
        for i in range(n):
            if bit & (1 << i):  # i番目のビットが立っているかチェック
                subset_sum += nums[i]  # 立っていれば要素を選択して和に加算

        if subset_sum == target:  # 部分集合の和が目標値と一致
            return True

    return False  # すべての部分集合をチェックしても見つからない場合
