def dfs(start):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(v)


n, s = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j + 1)

visited = [False] * (n + 1)
dfs(s)
print(sum(visited))
