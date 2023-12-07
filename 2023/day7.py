from collections import Counter
from functools import cmp_to_key

scores = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

part = 1

def get_type1(h):
    c = Counter(h)

    match sorted(c.values()):
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case _:
            return 1
        
def get_type2(h):
    c = Counter(h)


    j_count = c["J"]
    del c["J"]
    if len(c) == 0:
        c["A"] = 5
    else:
        mc, _ = c.most_common()[0]
        c[mc] += j_count

    match sorted(c.values()):
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case _:
            return 1
        
def key1(hb):
    h = hb[0]
    t = get_type1(h)
    return [t] + [scores[c] for c in h]

def key2(hb):
    h = hb[0]
    t = get_type2(h)
    return [t] + [scores[c] for c in h]


def get_winnings1(hand_bids):
    in_order = sorted(hand_bids, key=key1)
    total = 0
    rank = 1
    for _, bid in in_order:
        total += bid * rank
        rank += 1
    return total

def get_winnings2(hand_bids):
    in_order = sorted(hand_bids, key=key2)
    total = 0
    rank = 1
    for _, bid in in_order:
        total += bid * rank
        rank += 1
    return total

def solve_part_1(input_data):
    lines = input_data.splitlines()
    hand_bids = []

    for hand in lines:
        hand, b = hand.split()
        hand_bids.append((hand, int(b)))
        
    return get_winnings1(hand_bids)

def solve_part_2(input_data):
    scores["J"] = 0
    
    lines = input_data.splitlines()
    hand_bids = []

    for hand in lines:
        hand, b = hand.split()
        hand_bids.append((hand, int(b)))
        
    return get_winnings2(hand_bids)