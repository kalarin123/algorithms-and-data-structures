from collections import deque
from sys import stdin

n, x1, y1, x2, y2 = map(int, stdin.read().split())
INF = 10 ** 9
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1)]

dist = [[INF] * (n + 1) for i in range(n + 1)]
pred = [[None] * (n + 1) for i in range(n + 1)]
dist[x1][y1] = 0
q = deque([(x1, y1)])

while q:
    x, y = q.popleft()
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            if dist[nx][ny] == INF:
                dist[nx][ny] = dist[x][y] + 1
                pred[nx][ny] = (x, y)
                q.append((nx, ny))

print(dist[x2][y2])
path = []
node = (x2, y2)
while node is not None:
    path.append(node)
    x, y = node
    node = pred[x][y]

for x, y in path[::-1]:
    print(x, y)
