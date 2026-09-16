import sys


def SelectionSort(A):
    for i in range(len(A) - 1):
        max_index = i

        for j in range(i + 1, len(A)):
            if A[j] > A[max_index]:
                max_index = j

        A[i], A[max_index] = A[max_index], A[i]

    return A


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    print(*SelectionSort(numbers))


if __name__ == "__main__":
    main()
