import sys
import heapq

input = sys.stdin.buffer.readline
n = int(input())
heap = list(map(int, sys.stdin.buffer.read().split()))
heapq.heapify(heap)
total = 0

for _ in range(n - 1):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    s = x + y
    total += s
    heapq.heappush(heap, s)

print(f'{total * 0.05:.2f}')

