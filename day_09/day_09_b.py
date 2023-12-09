with open(r'real_data2.txt') as f:
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
    r[0].insert(0, 0)
    for i in range(1, len(r)):
        r[i].insert(0, r[i][0] - r[i-1][0])

answer = sum([r[-1][0] for r in res])
print(answer) # 867