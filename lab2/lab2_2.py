def nearest(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    pos = left

    if pos == 0:
        return arr[0]
    if pos == len(arr):
        return arr[-1]

    left_value = arr[pos - 1]
    right_value = arr[pos]

    if x - left_value <= right_value - x:
        return left_value
    return right_value


n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    print(nearest(arr, x))
