def solve_part_1(input_data):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_data.strip().split("\n"):
        actions = line.split(" ")
        if actions[0] == 'turn':
            state, from_coor, _, to_coor = actions[1:]
        else:
            state, from_coor, _, to_coor = actions
        from_x, from_y = [int(n) for n in from_coor.split(",")]
        to_x, to_y = [int(n) for n in to_coor.split(",")]
        if state == 'toggle':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] = not matrix[y][x]
        elif state == 'off':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] = 0
        elif state == 'on':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] = 1
    total_count = 0
    for x_list in matrix:
        total_count += x_list.count(1)
    return total_count


def solve_part_2(input_data):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_data.strip().split("\n"):
        actions = line.split(" ")
        if actions[0] == 'turn':
            state, from_coor, _, to_coor = actions[1:]
        else:
            state, from_coor, _, to_coor = actions
        from_x, from_y = [int(n) for n in from_coor.split(",")]
        to_x, to_y = [int(n) for n in to_coor.split(",")]
        if state == 'toggle':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] += 2
        elif state == 'off':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] -= 1
                    if matrix[y][x] < 0:
                        matrix[y][x] = 0
        elif state == 'on':
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):
                    matrix[y][x] += 1
    total_count = 0
    for x_list in matrix:
        total_count += sum(x_list)
    return total_count