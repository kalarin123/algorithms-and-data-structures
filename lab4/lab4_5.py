import sys

n = int(sys.stdin.buffer.readline())
a = list(map(int, sys.stdin.buffer.read().split()))
cost = 0
while len(a) > 1:
    a.sort()
    x = a.pop(0)
    y = a.pop(0)
    cost += (x + y) * 0.05
    a.append(x + y)
print(f'{cost:.2f}')

