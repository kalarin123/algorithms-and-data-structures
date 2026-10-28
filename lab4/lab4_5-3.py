import sys
import heapq

n = int(sys.stdin.buffer.readline())
a = [-x for x in map(int, sys.stdin.buffer.read().split())]
heapq.heapify(a)
cost = 0
for _ in range(n - 1):
    x = -heapq.heappop(a)
    y = -heapq.heappop(a)
    cost += (x + y) * 0.05
    heapq.heappush(a, -(x + y))
print(f'{cost:.2f}')

