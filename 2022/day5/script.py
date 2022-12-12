with open("./data") as f:
    lines = f.read().split("\n")


def purpose_data():
    split_index = -1
    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            split_index = i
            break
    crates_array = lines[:split_index]
    crates_array.reverse()
    crate_indexes = [crates_array[0].index(char) for char in crates_array[0] if char != " "]
    crates = []
    for index in crate_indexes:
        crates.append([])
        for line in crates_array[1:]:
            if line[index] != " ":
                crates[-1].append(line[index])
    moves = lines[split_index + 1:]
    moves = [move.split(" ") for move in moves]
    moves = [(int(amount), int(from_stack)-1, int(to_stack)-1) for _, amount, _, from_stack, _, to_stack in moves]
    return crates, moves


# purpose_data()
def run1():
    crates, moves = purpose_data()
    for amount, from_stack, to_stack in moves:
        for _ in range(int(amount)):
            crates[int(to_stack)].append(crates[int(from_stack)].pop())
    result = ""
    for stack in crates:
        result += stack[-1]
    print(result)


def run2():
    crates, moves = purpose_data()
    for amount, from_stack, to_stack in moves:
        to_move = crates[from_stack][-amount:]
        crates[to_stack].extend(to_move)
        del crates[from_stack][-amount:]
    result = ""
    for stack in crates:
        result += stack[-1]
    print(result)


if __name__ == "__main__":
    run1()
    run2()
