import sys

n = int(sys.stdin.buffer.readline())
a = list(map(int, sys.stdin.buffer.read().split()))
for i in range(1, n):
    x = a[i]
    j = i - 1
    while j >= 0 and a[j] > x:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x
print(*a)

