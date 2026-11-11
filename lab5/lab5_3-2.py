import sys
numbers = list(map(int, sys.stdin.buffer.read().split()))
print(sum(x != 0 for x in numbers[:numbers.index(0)]))
