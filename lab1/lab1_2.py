def InsertionSort(A):
    n = len(A)

    for i in range(1, n):
        x = A[i]
        j = i - 1

        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = x


A = list(map(int, input().split()))

InsertionSort(A)

print(*A)
