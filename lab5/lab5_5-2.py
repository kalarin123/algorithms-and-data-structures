import sys
seen = set()
for x in map(int, sys.stdin.buffer.read().split()):
    if x == 0: break
    if x not in seen:
        print(x)
        seen.add(x)
