def solve_part_1(input_data):
    current_floor = 0
    action_arr = list(input_data)
    for action in action_arr:
        if action == '(':
            current_floor += 1
        else:
            current_floor -= 1
    return current_floor


def solve_part_2(input_data):
    curr_char = 1
    curr_floor = 0
    action_arr = list(input_data)

    for action in action_arr:
        if action == '(':
            curr_floor += 1
        else:
            curr_floor -= 1
        if curr_floor < 0:
            return curr_char
        curr_char += 1
    return 0