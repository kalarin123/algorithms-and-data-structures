import sys


def Merge(A, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= right:
        temp.append(A[j])
        j += 1

    for k in range(len(temp)):
        A[left + k] = temp[k]


def MergeSort(A, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    MergeSort(A, left, mid)
    MergeSort(A, mid + 1, right)
    Merge(A, left, mid, right)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    A = data[1:1 + n]

    MergeSort(A, 0, n - 1)
    print(*A)


if __name__ == "__main__":
    main()
