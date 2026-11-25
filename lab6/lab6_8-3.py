from collections import deque

INF = 10 ** 9

n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j + 1)

s, t = map(int, input().split())
dist = [INF] * (n + 1)
dist[s] = 0
pred = [-1] * (n + 1)
q = deque([s])

while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if dist[neighbor] == INF:
            dist[neighbor] = dist[node] + 1
            pred[neighbor] = node
            q.append(neighbor)

if dist[t] == INF:
    print(-1)
else:
    print(dist[t])
    if dist[t] > 0:
        path = []
        ver = t
        while ver != -1:
            path.append(ver)
            ver = pred[ver]
        print(*path[::-1])
