import sys
import heapq

input = sys.stdin.buffer.readline
n = int(input())
fish = [int(input()) for _ in range(n)]

events = []
for i, count in enumerate(fish):
    first = max(1000 - count, 1)
    heapq.heappush(events, (first, i, count + 1))

previous_time = 0
position = 0
while events:
    time, i, count = heapq.heappop(events)
    if abs(i - position) > time - previous_time:
        print(time)
        break

    previous_time = time
    position = i
    next_time = time + max(1000 - count, 1)
    heapq.heappush(events, (next_time, i, count + 1))

