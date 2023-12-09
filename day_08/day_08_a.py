from dataclasses import dataclass
    
with open(r'real_data.txt') as f:
    instructions = f.readline()
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

# print(elements)
from itertools import cycle

e = elements['AAA']
num_steps = 0
for i in cycle(instructions):
    print(f'Element {e}')

    if i == 'L':
        e = elements[e.left]
        num_steps += 1
    elif i == 'R':
        e = elements[e.right]
        num_steps += 1
    if e.current == 'ZZZ':
        break
    print(num_steps)


print(num_steps)


