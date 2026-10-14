import sys
from collections import deque

n = int(sys.stdin.buffer.readline())
left = deque()
right = deque()
result = []

for _ in range(n):
    parts = sys.stdin.buffer.readline().split()
    command = parts[0]

    if command == b'+':
        right.append(int(parts[1]))
    elif command == b'*':
        left.append(int(parts[1]))
    else:
        result.append(str(left.popleft()))

    if len(left) < len(right):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())

sys.stdout.write('\n'.join(result))
