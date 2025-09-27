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
    return -1
