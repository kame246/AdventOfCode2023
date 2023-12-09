import math
from dataclasses import dataclass
from itertools import cycle

with open(r'real_data2.txt') as f:
    instructions = f.readline().strip()
    f.readline()
    data = f.readlines()

@dataclass
class Element:
    left: str
    right: str

elements = {}
for d in data:
    c, lr = d.split('=')
    current = c.strip()
    left, right = lr.strip().replace('(', '').replace(')', '').split(',')
    elements[current] = Element(left.strip(), right.strip())

num_steps = 0
elems = {k for k in elements if k.endswith('A')}
steps = []
for e in elems:
    num_steps = 0
    for i in cycle(instructions):
        e = elements[e].left if i == 'L' else elements[e].right
        num_steps += 1
        if e.endswith('Z'):
            steps.append(num_steps)
            break

def nww(a, b):
    return (a * b) // math.gcd(a, b)

def nww_numbers(numbers):
    result = nww(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        result = nww(result, numbers[i])
    return result

print(f'{nww_numbers(steps)}') # 18024643846273