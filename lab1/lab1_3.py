n = int(input())
A = list(map(int, input().split()))

swaps = 0

for i in range(n - 1):
    for j in range(n - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            swaps += 1

print(swaps)
