n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = True
for i in range(n):
    if a[i][i] != 0:
        ans = False
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            ans = False

if ans:
    print('YES')
else:
    print('NO')
