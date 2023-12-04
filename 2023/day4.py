def solve_part_1(input_data):
    lines = input_data.split("\n")
    total_score = 0
    for line in lines:
        card_number, both_cards = line.strip().split(": ")
        winning_numbers_str, scratched_numbers_str = both_cards.split(" | ")
        winning_numbers = [wn for wn in winning_numbers_str.strip().split(" ") if len(wn) > 0]
        scratched_numbers = [sn for sn in scratched_numbers_str.strip().split(" ") if len(sn) > 0]
        card_score = 0
        for number in winning_numbers:
            if number in scratched_numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        total_score += card_score
    return total_score
   
def calculate_score(card_num, list_of_cards):
    card_count = 1
    for card in list_of_cards[card_num]:
        card_count += calculate_score(card, list_of_cards)
    return card_count

def solve_part_2(input_data):
    # winning_number_per_card = {}
    # lines = input_data.split("\n")
    # for line in lines:
    #     card_number, both_cards = line.strip().split(": ")
    #     card_num = int(card_number.split(" ")[-1])
    #     winning_number_per_card[card_num] = []
    #     winning_numbers_str, scratched_numbers_str = both_cards.split(" | ")
    #     winning_numbers = [int(wn) for wn in winning_numbers_str.strip().split(" ") if len(wn) > 0]
    #     scratched_numbers = [int(sn) for sn in scratched_numbers_str.strip().split(" ") if len(sn) > 0]
    #     for number in winning_numbers:
    #         if number in scratched_numbers:
    #             winning_number_per_card[card_num].append(number)
    
    # total_score = 0
    # print(winning_number_per_card)
    # for key in winning_number_per_card:
    #     total_score += calculate_score(key, winning_number_per_card)
    # return total_score
    
    d=[p.split(": ")[1].split(" | ")for p in input_data.split("\n")]
    r=lambda t:range(sum([z in d[t][0].split()for z in d[t][1].split()]))
    v=lambda t:sum([1+v(t+x+1)for x in r(t)])
    return sum([1+v(d.index(k))for k in d])
    
    
    
    