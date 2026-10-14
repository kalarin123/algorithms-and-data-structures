import sys

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def back(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


stack = Stack()
answers = []
for line in sys.stdin:
    command = line.split()
    if not command:
        continue
    if command[0] == 'push':
        stack.push(int(command[1]))
        answers.append('ok')
    elif command[0] == 'pop':
        value = stack.pop()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'back':
        value = stack.back()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'size':
        answers.append(str(stack.size()))
    elif command[0] == 'clear':
        stack.clear()
        answers.append('ok')
    elif command[0] == 'exit':
        answers.append('bye')
        break
print('\n'.join(answers))
