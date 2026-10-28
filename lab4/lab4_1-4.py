import sys

def add(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0:
        p = (i - 1) // 2
        if a[p] >= a[i]:
            break
        a[i], a[p] = a[p], a[i]
        i = p

def extract(a):
    result = a[0]
    last = a.pop()
    if not a:
        return result

    a[0] = last
    i = 0
    n = len(a)
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and a[j + 1] > a[j]:
            j += 1
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j
    return result

input = sys.stdin.buffer.readline
n = int(input())
a = []
ans = []
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        add(a, cmd[1])
    else:
        ans.append(str(extract(a)))
sys.stdout.write('\n'.join(ans))

