import sys

class Queue:
    def __init__(self):
        self.left = []
        self.right = []

    def is_empty(self):
        return not self.left and not self.right

    def move(self):
        if not self.right:
            while self.left:
                self.right.append(self.left.pop())

    def push(self, item):
        self.left.append(item)

    def pop(self):
        self.move()
        if not self.right:
            return None
        return self.right.pop()

    def front(self):
        self.move()
        if not self.right:
            return None
        return self.right[-1]

    def size(self):
        return len(self.left) + len(self.right)

    def clear(self):
        self.left.clear()
        self.right.clear()


queue = Queue()
answers = []
for line in sys.stdin:
    command = line.split()
    if not command:
        continue
    if command[0] == 'push':
        queue.push(int(command[1]))
        answers.append('ok')
    elif command[0] == 'pop':
        value = queue.pop()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'front':
        value = queue.front()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'size':
        answers.append(str(queue.size()))
    elif command[0] == 'clear':
        queue.clear()
        answers.append('ok')
    elif command[0] == 'exit':
        answers.append('bye')
        break
print('\n'.join(answers))
