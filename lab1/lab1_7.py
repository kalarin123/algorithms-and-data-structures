class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def DistanceSquared(point):
    return point.x * point.x + point.y * point.y


n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

points.sort(key=DistanceSquared)

for point in points:
    print(point.x, point.y)
