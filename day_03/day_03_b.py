with open(r'real_data.txt') as f:
    lines = [line.strip() for line in f]

max_cols = len(lines[0])
max_col = max_cols - 1
max_rows = len(lines)
max_row = max_rows - 1

EMPTY = '.'

potential_gears = []
def is_adjacent(row, col, lines):
    if row > 0 and col > 0 and lines[row - 1][col - 1] != EMPTY and not lines[row - 1][col - 1].isdigit() and lines[row - 1][col - 1] == '*': # TOP LEFT CORNER
        return (row - 1, col - 1)
    elif row > 0 and col < max_col - 1 and lines[row - 1][col + 1] != EMPTY and not lines[row - 1][col + 1].isdigit() and lines[row - 1][col + 1] == '*': # TOP RIGHT CORNER
        return (row - 1, col + 1)
    elif col < max_col - 1 and lines[row][col + 1] != EMPTY and not lines[row][col + 1].isdigit() and lines[row][col + 1] == '*':  # RIGHT
        return (row, col + 1)
    elif col > 0 and lines[row][col - 1] != EMPTY and not lines[row][col - 1].isdigit() and lines[row][col - 1] == '*':  # LEFT
        return (row, col - 1)
    elif row < max_row - 1 and lines[row + 1][col] != EMPTY and not lines[row + 1][col].isdigit() and lines[row + 1][col] == '*':  # BOTTOM   xxxxx
        return (row + 1, col)
    elif row > 0 and lines[row - 1][col] != EMPTY and not lines[row - 1][col].isdigit() and lines[row - 1][col] == '*':  # TOP
        return (row - 1, col)
    elif col > 0 and row < max_row - 1 and lines[row + 1][col - 1] != EMPTY and not lines[row + 1][col - 1].isdigit() and lines[row + 1][col - 1] == '*':  # BOTTOM LEFT CORNER
        return (row + 1, col - 1)
    elif col < max_col - 1 and row < max_row - 1 and lines[row + 1][col + 1] != EMPTY and not lines[row + 1][col + 1].isdigit() and lines[row + 1][col + 1] == '*':  # BOTTOM RIGHT CORNER
        return (row + 1, col + 1)
    else:
        return None


row = 0
while row < max_rows:
    col = 0
    while col < max_cols:
        num = ''
        s = set()
        while col < max_cols and lines[row][col].isdigit():
            num += lines[row][col]
            is_adj = is_adjacent(row, col, lines)
            if is_adj is not None:
                s.add(is_adj)
            col += 1
        for x in s:
            potential_gears.append((x, int(num)))
        col += 1
    row += 1

r = {}
for gear in potential_gears:
    dane, n = gear
    r[dane] = r.get(dane, []) + [n]

result = sum([v[0] * v[1] for v in r.values() if len(v) == 2])
print(f'Answer: {result}') # 80694070