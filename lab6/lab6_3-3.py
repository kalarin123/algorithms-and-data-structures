n, m = map(int, input().split())
a = [[0] * n for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1][v - 1] = 1
    a[v - 1][u - 1] = 1

ans = True
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == 0:
            ans = False

if ans:
    print('YES')
else:
    print('NO')
