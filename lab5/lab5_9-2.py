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
heights = [0] * len(keys)
if root == -1:
    print('YES')
else:
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not visited:
            stack.append((node, True))
            if left[node] != -1: stack.append((left[node], False))
            if right[node] != -1: stack.append((right[node], False))
        else:
            hl = heights[left[node]] if left[node] != -1 else 0
            hr = heights[right[node]] if right[node] != -1 else 0
            heights[node] = 1 + max(hl, hr)
l = heights[left[root]] if left[root] != -1 else 0
r = heights[right[root]] if right[root] != -1 else 0
print('YES' if abs(l-r) <= 1 else 'NO')
