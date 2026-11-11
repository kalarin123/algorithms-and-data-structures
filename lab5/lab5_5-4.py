import sys

def build_tree():
    first = {}
    for x in map(int, sys.stdin.buffer.read().split()):
        if x == 0:
            break
        if x not in first:
            first[x] = len(first)

    keys = sorted(first)
    n = len(keys)
    order = [first[x] for x in keys]
    left = [-1] * n
    right = [-1] * n
    stack = []

    for i in range(n):
        last = -1
        while stack and order[stack[-1]] > order[i]:
            last = stack.pop()
        if stack:
            right[stack[-1]] = i
        if last != -1:
            left[i] = last
        stack.append(i)

    root = stack[0] if stack else -1
    return keys, left, right, root

keys, left, right, root = build_tree()
stack = []
cur = root
result = []
while cur != -1 or stack:
    while cur != -1:
        stack.append(cur)
        cur = left[cur]
    cur = stack.pop()
    result.append(str(keys[cur]))
    cur = right[cur]
sys.stdout.write('\n'.join(result))
