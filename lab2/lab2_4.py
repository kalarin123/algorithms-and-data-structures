a, b, c, d = map(int, input().split())


def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


left = -1001.0
right = 1001.0

for _ in range(100):
    mid = (left + right) / 2

    if f(left) * f(mid) <= 0:
        right = mid
    else:
        left = mid

print(f"{(left + right) / 2:.10f}")
