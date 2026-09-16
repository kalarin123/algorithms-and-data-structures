def SelectionSort(A):
    n = len(A)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if A[j] > A[max_index]:
                max_index = j

        A[i], A[max_index] = A[max_index], A[i]


A = list(map(int, input().split()))

SelectionSort(A)

print(*A)
