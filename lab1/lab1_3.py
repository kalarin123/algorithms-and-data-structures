import sys


def BubbleSort(A):
    n = len(A)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] < A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    print(*BubbleSort(numbers))


if __name__ == "__main__":
    main()
