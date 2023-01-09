def solve_part_1(input_data: str) -> int:
    # Parse the input data
    measurements = [int(x) for x in input_data.strip().split('\n')]

    # Count the number of times a depth measurement increases from the previous measurement
    count = 0
    prev = measurements[0]
    for measurement in measurements[1:]:
        if measurement > prev:
            count += 1
        prev = measurement

    return count


def solve_part_2(input_data: str) -> int:
    # Parse the input data
    measurements = [int(x) for x in input_data.strip().split('\n')]

    # Count the number of times the sum of a three-measurement window is larger than the previous sum
    count = 0
    prev = 0
    for i in range(2, len(measurements)):
        window_sum = sum(measurements[i-2:i+1])
        if window_sum > prev:
            count += 1
        prev = window_sum

    return count
