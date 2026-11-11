import sys

class Node:
    __slots__ = ('value', 'left', 'right', 'count')

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

def build_tree():
    root = None
    size = 0
    for x in map(int, sys.stdin.buffer.read().split()):
        if x == 0:
            break
        if root is None:
            root = Node(x)
            size += 1
            continue
        cur = root
        while True:
            if x == cur.value:
                cur.count += 1
                break
            if x < cur.value:
                if cur.left is None:
                    cur.left = Node(x)
                    size += 1
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(x)
                    size += 1
                    break
                cur = cur.right
    return root, size

def inorder(root):
    out = []
    stack = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur)
        cur = cur.right
    return out

root, count = build_tree()
height = 0
if root:
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        height = max(height, depth)
        if node.left: stack.append((node.left, depth + 1))
        if node.right: stack.append((node.right, depth + 1))
print(height)
