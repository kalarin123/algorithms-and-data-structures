import sys

def add(a, x):
    a.append(x)
    i = len(a) - 1
    while i:
        p = (i - 1) // 2
        if a[p] >= a[i]:
            break
        a[p], a[i] = a[i], a[p]
        i = p

def pop_max(a):
    x = a[0]
    last = a.pop()
    if a:
        a[0] = last
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
numbers = list(map(int, sys.stdin.buffer.read().split()))
heap = []
for x in numbers:
    add(heap, x)
print(*(pop_max(heap) for _ in range(n)))

