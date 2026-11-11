import sys

def get_frequency():
    freq = {}
    first = {}
    for x in map(int, sys.stdin.buffer.read().split()):
        if x == 0:
            break
        if x not in freq:
            first[x] = len(first)
            freq[x] = 1
        else:
            freq[x] += 1
    return sorted(first), freq

keys, freq = get_frequency()
print(*(f'{key} 1' for key in keys), sep='\n')
