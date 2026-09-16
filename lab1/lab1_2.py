import sys


def InsertionSort(A):
    for i in range(1, len(A)):
        current = A[i]
        j = i - 1

        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = current

    return A


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    print(*InsertionSort(numbers))


if __name__ == "__main__":
    main()
