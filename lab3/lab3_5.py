import sys
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push_front(self, item):
        self.items.appendleft(item)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def pop_back(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def back(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


dq = Deque()
answers = []
for line in sys.stdin:
    command = line.split()
    if not command:
        continue
    if command[0] == 'push_front':
        dq.push_front(int(command[1]))
        answers.append('ok')
    elif command[0] == 'push_back':
        dq.push_back(int(command[1]))
        answers.append('ok')
    elif command[0] == 'pop_front':
        value = dq.pop_front()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'pop_back':
        value = dq.pop_back()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'front':
        value = dq.front()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'back':
        value = dq.back()
        answers.append('error' if value is None else str(value))
    elif command[0] == 'size':
        answers.append(str(dq.size()))
    elif command[0] == 'clear':
        dq.clear()
        answers.append('ok')
    elif command[0] == 'exit':
        answers.append('bye')
        break
print('\n'.join(answers))
