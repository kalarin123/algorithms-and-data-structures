import sys

input = sys.stdin.buffer.readline
n = int(input())
initial = [int(input()) for _ in range(n)]

previous_time = 0
position = 0
time = 1

while True:
    for i in range(n):
        count = initial[i]
        next_birth = 0
        while next_birth < time:
            next_birth += max(1000 - count, 1)
            count += 1

        if next_birth == time:
            if abs(i - position) > time - previous_time:
                print(time)
                sys.exit()
            position = i
            previous_time = time
    time += 1

