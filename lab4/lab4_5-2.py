import sys

n = int(sys.stdin.buffer.readline())
a = list(map(int, sys.stdin.buffer.read().split()))
s = a[0]
cost = 0
for i in range(1, n):
    s += a[i]
    cost += s * 0.05
print(f'{cost:.2f}')

