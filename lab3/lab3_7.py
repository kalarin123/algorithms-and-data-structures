import sys

numbers = list(map(int, sys.stdin.buffer.read().split()))
n = numbers[0]
wagons = numbers[1:n + 1]
stack = []
need = 1

for wagon in wagons:
    stack.append(wagon)
    while stack and stack[-1] == need:
        stack.pop()
        need += 1

print('YES' if need == n + 1 else 'NO')
