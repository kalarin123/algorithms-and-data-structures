import sys
import heapq

input = sys.stdin.buffer.readline
n = int(input())
fish = [int(input()) for _ in range(n)]
events = []
for i, count in enumerate(fish):
    heapq.heappush(events, (1000 - count, i, count + 1))

previous_time = 0
position = 0
while events:
    time, i, count = heapq.heappop(events)
    if abs(position - i) > time - previous_time:
        print(time)
        break
    position = i
    previous_time = time
    heapq.heappush(events, (time + max(1000 - count, 1), i, count + 1))

