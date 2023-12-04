result = 0
with open(r'real_data.txt') as f:
    lines = [line.strip() for line in f]

score = {}

for card_no, line in enumerate(lines, 1):
    _, cards = line.split(':')
    winning_cards, my_cards = cards.split('|')
    winning_cards = {int(x.strip()) for x in winning_cards.split(' ') if x}
    my_cards = {int(x.strip()) for x in my_cards.split(' ') if x}
    score[card_no] = len(winning_cards & my_cards)

res = dict.fromkeys(score.keys(), 1)

for card_no, cnt in score.items():
    for _ in range(res[card_no]):
        for i in range(1, cnt + 1):
            res[card_no + i] += 1

result = sum(res.values())
print(f'Answer: {result}') # 5539496