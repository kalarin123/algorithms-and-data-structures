from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

order = list(map(int, input().split()))
position = [0] * (n + 1)
for i in range(n):
    position[order[i]] = i

ans = True
for i in range(m):
    u, v = edges[i]
    if position[u] > position[v]:
        ans = False
        break

if ans:
    print('YES')
else:
    print('NO')
