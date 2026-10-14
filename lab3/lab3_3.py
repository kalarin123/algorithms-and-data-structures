import sys

stack = []

for token in sys.stdin.buffer.read().split():
    if token in (b'+', b'-', b'*'):
        right = stack.pop()
        left = stack.pop()
        if token == b'+':
            stack.append(left + right)
        elif token == b'-':
            stack.append(left - right)
        else:
            stack.append(left * right)
    else:
        stack.append(int(token))

print(stack[-1])
