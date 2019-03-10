h1 = list()
h2 = list()

with open('p054_poker.txt', 'r') as hands:
    for row in hands:
        row = row.replace('\n', '')
        row = row.replace('A', 'e').replace('K', 'd').replace('Q', 'c').replace('J', 'b').replace('T', 'a')
        h = row.split(' ')
        h1.append(h[:5])
        h2.append(h[5:])

Card = str
Hand = list

mult = 10**(2*5)

def card_value(c: Card) -> int:
    n = c[0]
    # if n == 'A':
    if n == 'e':
        return 14
    # if n == 'K':
    if n == 'd':
        return 13
    # if n == 'Q':
    if n == 'c':
        return 12
    # if n == 'J':
    if n == 'b':
        return 11
    # if n == 'T':
    if n == 'a':
        return 10
    return int(n)


def card_suit(c: Card) -> int:
    return c[1]


def high_card(hand: Hand) -> int:
    score = 0
    for c in hand:
        score = max(score, card_value(c))
    return score


def one_pair(hand: Hand) -> int:
    for i in range(1,len(hand)):
        for j in range(i):
            if card_value(hand[i]) == card_value(hand[j]):
                v = card_value(hand[i])
                del hand[i]
                del hand[j]
                return 1*mult + 100*v + high_card(hand)
    return 0


def two_pairs(hand: Hand) -> int:
    p = list()
    for i in range(1, len(hand)):
        for j in range(i):
            if card_value(hand[i]) == card_value(hand[j]):
                p.append(i)
                p.append(j)
    if len(p) != 4:
        return 0
    v = sorted([ card_value(hand[p[0]]), card_value(hand[p[2]]) ])
    for i in sorted(p, reverse=True):
        del hand[i]
    return 2*mult + 10000*v[1] + 100*v[0] + high_card(hand)


def three_of_a_kind(hand: Hand) -> int:
    for i in range(2, len(hand)):
        for j in range(1, i):
            for k in range(j):
                if card_value(hand[i]) == card_value(hand[j]) == card_value(hand[k]):
                    v = card_value(hand[i])
                    del hand[i]
                    del hand[j]
                    del hand[k]
                    return 3*mult + 100*v + high_card(hand)
    return 0


def straight(hand: Hand) -> int:
    hand.sort()
    for i in range(1, len(hand)):
        if card_value(hand[i]) - card_value(hand[i-1]) != 1:
            return 0
    return 4*mult + card_value(hand[4])


def flush(hand: Hand) -> int:
    suits = list(map(card_suit, hand))
    values = list(map(card_value, hand))
    suit = suits[0]
    for i in range(1, len(suits)):
        if suit != suits[i]:
            return 0
    values.sort()
    s = 5*mult
    m = 1
    for v in values:
        s += m*v
        m *= 100
    return s


def full_house(hand: Hand) -> int:
    for i in range(2, len(hand)):
        for j in range(1, i):
            for k in range(j):
                if card_value(hand[i]) == card_value(hand[j]) == card_value(hand[k]):
                    v = card_value(hand[i])
                    del hand[i]
                    del hand[j]
                    del hand[k]
                    if card_value(hand[0]) == card_value(hand[1]):
                        return 6*mult + 100*v + card_value(hand[0])
                    else:
                        return 0
    return 0


def four_of_a_kind(hand: Hand) -> int:
    for i in range(3, len(hand)):
        for j in range(2, i):
            for k in range(1, j):
                for l in range(k):
                    if card_value(hand[i]) == card_value(hand[j]) == card_value(hand[k]) == card_value(hand[l]):
                        del hand[i]
                        del hand[j]
                        del hand[k]
                        del hand[l]
                        return 7*mult + 100*card_value(hand[i]) + high_card(hand)
    return 0


def straight_flush(hand: Hand) -> int:
    s = straight(hand)
    if s and flush(hand):
        return 4*mult + s
    return 0


def royal_flush(hand: Hand) -> int:
    s = straight_flush(hand)
    if s == 8*mult + 14:
        return s + mult
    return 0


def eval_hand(hand: Hand) -> int:
    score = 0
    rf = royal_flush(list(hand))
    if rf:
        return rf
    sf = straight_flush(list(hand))
    if sf:
        return sf
    fk = four_of_a_kind(list(hand))
    if fk:
        return fk
    fh = full_house(list(hand))
    if fh:
        return fh
    fl = flush(list(hand))
    if fl:
        return fl
    st = straight(list(hand))
    if st:
        return st
    tk = three_of_a_kind(list(hand))
    if tk:
        return tk
    tp = two_pairs(list(hand))
    if tp:
        return tp
    op = one_pair(list(hand))
    if op:
        return op
    return high_card(list(hand))
    
c = 0
for i in range(1000):
    print(i)
    v1 = eval_hand(h1[i])
    v2 = eval_hand(h2[i])
    c += v1 > v2
print(c)