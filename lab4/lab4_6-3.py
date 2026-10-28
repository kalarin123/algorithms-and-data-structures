import sys
import heapq

input = sys.stdin.buffer.readline
n = int(input())
shipments = [tuple(map(int, input().split())) for _ in range(n)]
active = []
answer = 0
for t, length in shipments:
    while active and active[0] <= t:
        heapq.heappop(active)
    heapq.heappush(active, t + length)
    answer = max(answer, len(active))
print(answer)

