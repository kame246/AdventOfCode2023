result = 0
with open(r'real_data.txt') as f:
    lines = [line.strip() for line in f]

for card_no, line in enumerate(lines, 1):
    _, cards = line.split(':')
    winning_cards, my_cards = cards.split('|')
    winning_cards = {int(x.strip()) for x in winning_cards.split(' ') if x}
    my_cards = {int(x.strip()) for x in my_cards.split(' ') if x}
    common_len = len(winning_cards & my_cards)
    points = common_len if common_len < 2 else 2 ** (common_len - 1)
    result += points

print(f'Answer: {result}') # 21821