import sys

def add(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0:
        p = (i - 1) // 2
        if a[p] >= a[i]:
            break
        a[p], a[i] = a[i], a[p]
        i = p

def extract(a):
    result = a[0]
    last = a.pop()
    if a:
        a[0] = last
        i = 0
        while 2 * i + 2 < len(a):
            left = 2 * i + 1
            right = left + 1
            j = left if a[left] >= a[right] else right
            if a[i] >= a[j]:
                break
            a[i], a[j] = a[j], a[i]
            i = j
    return result

n = int(sys.stdin.buffer.readline())
heap = []
for _ in range(n):
    command = list(map(int, sys.stdin.buffer.readline().split()))
    if command[0] == 0:
        add(heap, command[1])
    else:
        print(extract(heap))

