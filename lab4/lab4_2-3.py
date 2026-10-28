import sys

def sift_down(a, i, size):
    while i * 2 + 1 < size:
        j = i * 2 + 1
        if j + 1 < size and a[j + 1] > a[j]:
            j += 1
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j

n = int(sys.stdin.buffer.readline())
a = list(map(int, sys.stdin.buffer.read().split()))
for i in range(n // 2 - 1, -1, -1):
    sift_down(a, i, n)
for end in range(n - 1, 1, -1):
    a[0], a[end] = a[end], a[0]
    sift_down(a, 0, end)
print(*a)

