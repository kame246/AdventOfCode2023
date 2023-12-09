with open(r'real_data.txt') as f:
    sequences = [[int(x.strip()) for x in row.split(' ') if x] for row in f.readlines()]

res = []
for sequence in sequences:
    results = [sequence]
    while True:
        if all(x == 0 for x in sequence):
            break
        sequence = [sequence[it] - sequence[it - 1] for it in range(1, len(sequence))]
        results.append(sequence)
    res.append(results)

for r in res:
    r.reverse()
    r[0].append(0)
    for i in range(1, len(r)):
        r[i].append(r[i-1][-1] + r[i][-1])

answer = sum([r[-1][-1] for r in res])
print(answer) # 1772145754
