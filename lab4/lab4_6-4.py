import sys
import heapq

input = sys.stdin.buffer.readline
n = int(input())
shipments = [tuple(map(int, input().split())) for _ in range(n)]
shipments.sort()

busy = []
answer = 0
for t, length in shipments:
    while busy and busy[0] <= t:
        heapq.heappop(busy)
    heapq.heappush(busy, t + length)
    answer = max(answer, len(busy))

print(answer)

