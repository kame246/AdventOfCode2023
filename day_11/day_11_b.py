with open('real_data.txt') as f:
    data = [list(x.strip()) for x in f.readlines()]

width = len(data[0])
height = len(data)
factor = 1000000

ins_rows_indexes = [index for index, row in enumerate(data) if '#' not in row]
ins_cols_indexes = [col for col in range(width) if not sum([1 for r in data if r[col] == '#'])]

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
    dy = 0
    y2, y1 = (y2, y1) if y2 > y1 else (y1, y2)
    for i in range(y1, y2):
        dy = dy + (factor if i in ins_rows_indexes else 1)

    dx = 0
    x2, x1 = (x2, x1) if x2 > x1 else (x1, x2)
    for i in range(x1, x2):
        dx = dx + (factor if i in ins_cols_indexes else 1)

    return dx + dy


distances = []
for pair in pairs:
    distances.append(count_distance(galaxies[pair[0]], galaxies[pair[1]]))

print(f'Answer:', sum(distances)) # 447073334102