def dfs(start):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(v)


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
dfs(1)

if sum(visited) == n and m == n - 1:
    print('YES')
else:
    print('NO')
