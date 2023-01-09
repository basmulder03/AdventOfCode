def solve_part_1(input: str) -> int:
    commands = [x.strip().split(" ") for x in input.splitlines()]

    # Follow the planned course
    horizontal_position = 0
    depth = 0
    for command, value in commands:
        value = int(value)
        if command == 'forward':
            horizontal_position += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value

    # Calculate the final horizontal position and depth and print the result
    final_horizontal_position = horizontal_position
    final_depth = depth
    result = final_horizontal_position * final_depth

    return result


def solve_part_2(input_string: str) -> int:
    # Parse the input
    commands = [x.strip().split() for x in input_string.strip().split('\n')]

    # Follow the planned course
    horizontal_position = 0
    depth = 0
    aim = 0
    for command, value in commands:
        value = int(value)
        if command == 'forward':
            horizontal_position += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    # Calculate the final horizontal position and depth and return the result
    final_horizontal_position = horizontal_position
    final_depth = depth
    result = final_horizontal_position * final_depth
    return result
