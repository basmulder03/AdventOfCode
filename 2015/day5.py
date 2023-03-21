def double_letter_count(input: str, amount: int) -> bool:
    chars = list(input)
    last_letter = chars[0]
    letter_amount = 1
    for char in chars[1:]:
        if char == last_letter:
            letter_amount += 1
            if letter_amount == amount:
                return True
        else:
            letter_amount = 1
            last_letter = char
    return False

def contains_amount_of_vowels(input: str, amount: int) -> bool:
    vowels = ['a', 'e', 'i', 'u', 'o']
    return len([x for x in list(input) if x in vowels]) >= amount

def does_not_contain_blacklist(input: str) -> bool:
    blacklist = ['ab', 'cd', 'pq', 'xy']
    for item in blacklist:
        if item in input:
            return False
    return True

def solve_part_1(input_data):
    nice_list = 0
    for line in input_data.strip().split("\n"):
        if double_letter_count(line, 2) and contains_amount_of_vowels(line, 3) and does_not_contain_blacklist(line):
            nice_list += 1
    return nice_list

def contains_double_pair(input: str) -> bool:
    pairs = {}
    pairs_at_index = {}
    input_list = list(input)
    for i in range(len(input_list)):
        if i + 1 < len(input_list):
            curr_pair = "".join(input_list[i: i+2])
            if pairs_at_index.setdefault(curr_pair, False):
                indices = pairs_at_index[curr_pair]
                if i in indices or i + 1 in indices:
                    continue
            pairs[curr_pair] = pairs.setdefault(curr_pair, 0) + 1
            pairs_at_index[curr_pair] = [i, i+1]
            if pairs[curr_pair] == 2:
                return True
    return False

def contains_letter_which_has_one_between(input: str) -> bool:
    input = list(input)
    last_letter = input[1]
    before_last_letter = input[0]
    for char in input[2:]:
        if char == before_last_letter:
            return True
        before_last_letter = last_letter
        last_letter = char
    return False


def solve_part_2(input_data):
    nice_list = 0
    for line in input_data.strip().split("\n"):
        if contains_double_pair(line) and contains_letter_which_has_one_between(line):
            nice_list += 1
    return nice_list
    