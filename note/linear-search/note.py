def subsetSum(numArr, target):
    n = len(numArr)
    for bit in range(1 << n):
        subset_sum = 0
        for i in range(n):
            if bit & (1 << i):
                subset_sum + numArr[i]
        if subset_sum == target:
            return True
    return False
