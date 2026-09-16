import sys


def QuickSort(A, left, right):
    i = left
    j = right
    pivot = A[(left + right) // 2]

    while i <= j:
        while A[i] < pivot:
            i += 1

        while A[j] > pivot:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    if left < j:
        QuickSort(A, left, j)

    if i < right:
        QuickSort(A, i, right)


data = list(map(int, sys.stdin.read().split()))
n = data[0]
A = data[1:1 + n]

if n > 0:
    QuickSort(A, 0, n - 1)

print(*A)
