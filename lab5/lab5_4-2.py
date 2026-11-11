import sys
numbers = []
for x in map(int, sys.stdin.buffer.read().split()):
    if x == 0: break
    numbers.append(x)
numbers.sort()
print(numbers[-2])
