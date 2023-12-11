from dataclasses import dataclass
from matplotlib.path import Path
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

with open(r'real_data.txt') as f:
    board = [list(x.strip()) for x in f.readlines()]

@dataclass
class Point:
    x: int
    y: int
    def __hash__(self):
        return hash((self.x, self.y))

width = len(board[0])
height = len(board)

point = [Point(r, c) for r in range(height) for c in range(width) if board[r][c] == 'S'].pop()
visited_points = [[0 for _ in range(width)] for _ in range(height)]

max_step = 0
best_path = []

def add_point_to_surrounding(surrounding, point):
    try:
        if not visited_points[point.x][point.y] and board[point.x][point.y] != '.':
            surrounding.append(Point(point.x, point.y))
    except IndexError:
        pass

def check_position(point: Point, step, path):
    my_path = path + [point]
    surrounding = []
    global max_step
    if step > max_step:
        max_step = step
        global best_path
        best_path = my_path
    if visited_points[point.x][point.y]:
        return
    visited_points[point.x][point.y] = 1
    left, right, top, bottom = (
        Point(point.x, point.y - 1),
        Point(point.x, point.y + 1),
        Point(point.x - 1, point.y),
        Point(point.x + 1, point.y)
    )
    match board[point.x][point.y]:
        case 'S':
            add_point_to_surrounding(surrounding, left)
            add_point_to_surrounding(surrounding, right)
            add_point_to_surrounding(surrounding, top)
            add_point_to_surrounding(surrounding, bottom)
        case '-':
            add_point_to_surrounding(surrounding, left)
            add_point_to_surrounding(surrounding, right)
        case '|':
            add_point_to_surrounding(surrounding, top)
            add_point_to_surrounding(surrounding, bottom)
        case '7':
            add_point_to_surrounding(surrounding, left)
            add_point_to_surrounding(surrounding, bottom)
        case 'J':
            add_point_to_surrounding(surrounding, left)
            add_point_to_surrounding(surrounding, top)
        case 'L':
            add_point_to_surrounding(surrounding, top)
            add_point_to_surrounding(surrounding, right)
        case 'F':
            add_point_to_surrounding(surrounding, bottom)
            add_point_to_surrounding(surrounding, right)
    for neighbour in surrounding[::-1]:
        check_position(neighbour, step+1, my_path)

check_position(point, 0, best_path)
print('Answer to part 1:', sum(divmod(max_step, 2)))

result = 0
best_points = [(p.x, p.y) for p in best_path]
poly = Path(best_points)
for r in range(height):
    for c in range(width):
        result += (c, r) not in best_points and poly.contains_point((c, r))

plt.fill([p.x for p in best_path] + [best_path[0].x], [p.y for p in best_path] + [best_path[0].y])
plt.show()
print('Answer to part 2:', result)