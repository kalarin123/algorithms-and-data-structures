import sys

data = sys.stdin.buffer
n = int(data.readline())
a = []
for _ in range(n):
    command = list(map(int, data.readline().split()))
    if command[0] == 0:
        a.append(command[1])
    else:
        x = max(a)
        print(x)
        a.remove(x)

