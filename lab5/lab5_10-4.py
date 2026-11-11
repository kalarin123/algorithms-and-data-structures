import sys


def build_tree():
    first = {}
    count = {}
    for x in map(int, sys.stdin.buffer.read().split()):
        if x == 0:
            break
        if x not in first:
            first[x] = len(first)
            count[x] = 1
        else:
            count[x] += 1

    keys = sorted(first)
    order = [first[x] for x in keys]
    n = len(keys)
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
    return keys, left, right, root, count


keys, left, right, root, count = build_tree()
stack = []
node = root
answer = []
while node != -1 or stack:
    while node != -1:
        stack.append(node)
        node = left[node]
    node = stack.pop()
    answer.append(f'{keys[node]} {count[keys[node]]}')
    node = right[node]
sys.stdout.write('\n'.join(answer))
