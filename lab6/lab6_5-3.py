from sys import stdin

input = stdin.readline


def dfs(start):
    stack = [start]
    visited[start] = True
    component = []

    while stack:
        node = stack.pop()
        component.append(node)
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    return component


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
ans = []
for v in range(1, n + 1):
    if not visited[v]:
        ans.append(dfs(v))

print(len(ans))
for component in ans:
    print(len(component))
    print(*component)
