import sys

s = sys.stdin.readline().strip()
stack = []
matching = {')': '(', ']': '[', '}': '{'}
valid = True

for char in s:
    if char in '([{':
        stack.append(char)
    elif char in matching:
        if not stack or stack[-1] != matching[char]:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

print('yes' if valid else 'no')
