with open('real_data.txt') as f:
    data = [list(x.strip()) for x in f.readlines()]

width = len(data[0])
height = len(data)
ins_rows_indexes = [index for index, row in enumerate(data) if '#' not in row]
ins_cols_indexes = [col for col in range(width) if not sum([1 for r in data if r[col] == '#'])]

r = 0
for i in ins_rows_indexes:
    data.insert(i + r, data[i + r].copy())
    r += 1

for row in data:
    r = 0
    for i in ins_cols_indexes:
        row.insert(i + r, '.')
        r += 1

width = len(data[0])
height = len(data)

n = 1
galaxies = {}
for h in range(height):
    for w in range(width):
        if data[h][w] == '#':
            galaxies[n] = (w, h)
            n += 1

pairs = [(x, y) for i, x in enumerate(galaxies) for y in list(galaxies.keys())[i+1:]]

def count_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(y2 - y1) + abs(x2 - x1)


distances = []
for pair in pairs:
    distances.append(count_distance(galaxies[pair[0]], galaxies[pair[1]]))

print(f'Answer:', sum(distances)) # 10228230