import sys


def CountSort(A):
    count = [0] * 101

    for value in A:
        count[value] += 1

    position = 0

    for value in range(101):
        while count[value] > 0:
            A[position] = value
            position += 1
            count[value] -= 1

    return A


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    print(*CountSort(numbers))


if __name__ == "__main__":
    main()
