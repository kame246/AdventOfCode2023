from collections import Counter

figures = list('AKQJT98765432')
    
with open(r'real_data.txt') as f:
    lines = f.readlines()

hands = []
bids = []

for line in lines:
    hand, bid = line.split(' ')
    hand = hand.strip()
    bids.append(int(bid.strip()))
    hands.append(hand.replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', 'C').replace('T', 'B'))

max_rank = len(hands)

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

lists = [five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card]

for hand in hands:
    cnt = Counter(hand)
    vals = sorted(list(cnt.values()), reverse=True)
    if len(cnt.values()) == 1: # five of a kind
        five_of_kind.append(hand)
    elif len(cnt.values()) == 2 and vals[0] == 4:
        four_of_kind.append(hand)
    elif len(cnt.values()) == 2 and vals[0] == 3 and vals[1] == 2:
        full_house.append(hand)
    elif len(cnt.values()) == 3 and vals[0] == 3:
        three_of_kind.append(hand)
    elif len(cnt.values()) == 3 and vals[0] == 2 and vals[1] == 2:
        two_pair.append(hand)
    elif len(cnt.values()) == 4 and vals[0] == 2:
        one_pair.append(hand)
    elif len(cnt.values()) == 5:
        high_card.append(hand)

rank = max_rank
result = 0
for k in lists:
    k.sort(reverse=True)
    for cards in k:
        result += rank * bids[hands.index(cards)]
        rank -= 1

print(result)