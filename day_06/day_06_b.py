import math

with open(r'real_data.txt') as f:
    time_line, distance_line = f.readlines()
    times = [int(''.join([x.strip() for x in time_line.split(':')[1].split(' ') if x]))]
    distances = [int(''.join([x.strip() for x in distance_line.split(':')[1].split(' ') if x]))]


def find_press_ms(rng):
    for press_ms in rng:
        time_to_travel = t - press_ms
        d = press_ms * time_to_travel
        if d > distances[iteration]:
            return press_ms


results = []
for iteration, t in enumerate(times):
    ranges = (range(1, t), range(t - 1, 1, -1))
    minimum = find_press_ms(range(1, t))
    maximum = find_press_ms(range(t - 1, 0, -1))
    results.append(maximum - minimum + 1)

print(f'Answer: {math.prod(results)}')  # 37286485