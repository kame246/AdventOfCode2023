result = 0
with open(r'real_data.txt') as f:
    lines = [line.strip() for line in f]

max_cols = len(lines[0])
max_col = max_cols - 1
max_rows = len(lines)
max_row = max_rows - 1

EMPTY = '.'

def is_adjacent(row, col, lines):
    if row > 0 and col > 0 and lines[row - 1][col - 1] != EMPTY and not lines[row - 1][col - 1].isdigit(): # TOP LEFT CORNER
        return True
    elif row > 0 and col < max_col - 1 and lines[row - 1][col + 1] != EMPTY and not lines[row - 1][col + 1].isdigit(): # TOP RIGHT CORNER
        return True
    elif col < max_col - 1 and lines[row][col + 1] != EMPTY and not lines[row][col + 1].isdigit():  # RIGHT
        return True
    elif col > 0 and lines[row][col - 1] != EMPTY and not lines[row][col - 1].isdigit():  # LEFT
        return True
    elif row < max_row - 1 and lines[row + 1][col] != EMPTY and not lines[row + 1][col].isdigit():  # BOTTOM
        return True
    elif row > 0 and lines[row - 1][col] != EMPTY and not lines[row - 1][col].isdigit():  # TOP
        return True
    elif col > 0 and row < max_row - 1 and lines[row + 1][col - 1] != EMPTY and not lines[row + 1][col - 1].isdigit():  # BOTTOM LEFT CORNER
        return True
    elif col < max_col - 1 and row < max_row - 1 and lines[row + 1][col + 1] != EMPTY and not lines[row + 1][col + 1].isdigit():  # BOTTOM RIGHT CORNER
        return True
    return False


row = 0
while row < max_rows:
    col = 0
    while col < max_cols:
        n = 0
        num = ''
        while col < max_cols and lines[row][col].isdigit():
            num += lines[row][col]
            n += is_adjacent(row, col, lines)
            col += 1
        if n > 0:
            result += int(num)
        col += 1
    row += 1

print(f'Answer: {result}') # 521601