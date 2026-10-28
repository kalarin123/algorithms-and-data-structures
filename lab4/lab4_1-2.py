import sys

def add(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i] > a[i // 2]:
        a[i], a[i // 2] = a[i // 2], a[i]
        i //= 2

def extract(a):
    x = a[0]
    a[0] = a[-1]
    a.pop()
    i = 0
    while 2 * i + 1 < len(a):
        j = 2 * i + 1
        if j + 1 < len(a) and a[j + 1] > a[j]:
            j += 1
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j
    return x

n = int(sys.stdin.buffer.readline())
heap = []
for _ in range(n):
    command = list(map(int, sys.stdin.buffer.readline().split()))
    if command[0] == 0:
        add(heap, command[1])
    else:
        print(extract(heap))

