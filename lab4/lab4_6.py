import sys

input = sys.stdin.buffer.readline
n = int(input())
shipments = [tuple(map(int, input().split())) for _ in range(n)]
shipments.sort()
active = []
answer = 0
for t, length in shipments:
    active = [end for end in active if end > t]
    active.append(t + length)
    answer = max(answer, len(active))
print(answer)

