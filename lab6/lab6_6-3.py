def dfs(v):
    global cycle
    color[v] = 'gray'
    for w in graph[v]:
        if color[w] == 'white':
            dfs(w)
        if color[w] == 'gray':
            cycle = True
    color[v] = 'black'


n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j + 1)

color = ['white'] * (n + 1)
cycle = False
for v in range(1, n + 1):
    if color[v] == 'white':
        dfs(v)

print(int(cycle))
