def CountSort(A):
    count = [0] * 101

    for value in A:
        count[value] += 1

    k = 0

    for value in range(101):
        while count[value] > 0:
            A[k] = value
            k += 1
            count[value] -= 1


A = list(map(int, input().split()))

CountSort(A)

print(*A)
