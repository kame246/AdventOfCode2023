import math

def update_game_results_for_color(color, result_set, game_set):
    if color in game_set:
        result_set[color] = max([game_set[color], result_set.get(color, 0)])


with open(r'real_data.txt') as f:
    result = 0
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

        result_set = {}
        for s in sets:
            update_game_results_for_color('blue', result_set, s)
            update_game_results_for_color('red', result_set, s)
            update_game_results_for_color('green', result_set, s)

        result += math.prod(result_set.values())
        game_no += 1

print(f'Answer: {result}') # 74229