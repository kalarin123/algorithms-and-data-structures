import sys

class MinStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        if self.is_empty():
            minimum = x
        else:
            minimum = min(x, self.items[-1][1])
        self.items.append((x, minimum))

    def pop(self):
        return self.items.pop()[0]

    def get_min(self):
        if self.is_empty():
            return float('inf')
        return self.items[-1][1]


class MinQueue:
    def __init__(self):
        self.left = MinStack()
        self.right = MinStack()

    def push(self, x):
        self.left.push(x)

    def pop(self):
        if self.right.is_empty():
            while not self.left.is_empty():
                self.right.push(self.left.pop())
        return self.right.pop()

    def get_min(self):
        return min(self.left.get_min(), self.right.get_min())


n, k = map(int, sys.stdin.buffer.readline().split())
values = list(map(int, sys.stdin.buffer.read().split()))
queue = MinQueue()
answers = []
for i, x in enumerate(values):
    queue.push(x)
    if i >= k - 1:
        answers.append(str(queue.get_min()))
        queue.pop()
print('\n'.join(answers))
