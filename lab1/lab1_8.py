import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def DistanceSquared(point):
    return point.x * point.x + point.y * point.y


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]

    points = []
    index = 1

    for _ in range(n):
        x = data[index]
        y = data[index + 1]
        points.append(Point(x, y))
        index += 2

    points.sort(key=DistanceSquared)

    for point in points:
        print(point.x, point.y)


if __name__ == "__main__":
    main()
