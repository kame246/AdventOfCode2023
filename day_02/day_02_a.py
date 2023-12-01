color_to_max_cubes = {'red': 12, 'green': 13, 'blue': 14}

result = 0
with open(r'real_data.txt') as f:
    game_no = 1
    for line in f:
        _, rest = line.split(':')
        sets = []
        for s in rest.split(';'):
            game_set = {}
            for p in [x.strip() for x in s.split(',')]:
                n, color = p.split(' ')
                n = int(n)
                game_set[color] = n
            sets.append(game_set)

        possible = True
        for s in sets:
            for color in color_to_max_cubes:
                if color in s and s[color] > color_to_max_cubes[color]:
                    possible = False
                    break

        if possible:
            result += game_no

        game_no += 1

print(f'Answer: {result}')