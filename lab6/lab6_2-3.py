n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

sources = []
sinks = []
for i in range(n):
    source = True
    sink = True
    for j in range(n):
        if a[j][i] == 1:
            source = False
        if a[i][j] == 1:
            sink = False
    if source:
        sources.append(i + 1)
    if sink:
        sinks.append(i + 1)

print(len(sources))
print(*sources)
print(len(sinks))
print(*sinks)
