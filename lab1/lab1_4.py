import sys


def BubbleSwapCount(A):
    swaps = 0
    n = len(A)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps += 1

    return swaps


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    A = data[1:1 + n]

    print(BubbleSwapCount(A))


if __name__ == "__main__":
    main()
