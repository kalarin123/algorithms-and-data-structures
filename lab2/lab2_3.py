import math

c = float(input())

left = 0.0
right = max(1.0, c)

for _ in range(100):
    mid = (left + right) / 2
    value = mid * mid + math.sqrt(mid)

    if value < c:
        left = mid
    else:
        right = mid

print(f"{right:.10f}")
