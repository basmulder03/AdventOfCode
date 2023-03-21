actions = {
    'RSHIFT': '>>',
    'LSHIFT': '<<',
    'OR': '|',
    'NOT': '~',
    'AND': '&',
    'XOR': '^'
}

operations_map = {}

def populate_map(line):
    split = line.split(" ")
    if split[0] == 'NOT':
        operations_map[split[-1]] = f"{actions[split[0]]} {split[1]}"
    elif split[1] == '->':
        operations_map[split[-1]] = split[0]
    else:
        first, action, second, _, result = split
        operations_map[result] = f"{first} {actions[action]} {second}"

def eval_expression(current_operation):
    print(current_operation)
    curr_op = operations_map[current_operation]
    word_test_split = curr_op.split(" ")
    variables_to_eval = []
    for word in word_test_split:
        if not word.isnumeric() and not word in actions.values():
            variables_to_eval.append(word)
    if not len(variables_to_eval):
        return eval(curr_op)
    else:
        for v in variables_to_eval:
            r = eval_expression(v)
            operations_map[current_operation].replace(v, str(r))

def solve_part_1(input_data):
    for line in input_data.strip().split("\n"):
        populate_map(line)
    value_to_find = 'a'
    return eval_expression(value_to_find)

def solve_part_2(input_data):
    pass