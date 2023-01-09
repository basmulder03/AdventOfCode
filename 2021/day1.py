# advent of code 2021 day 1

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
    measurements = [int(x) for x in input_data.strip().split('\n')]

    # Consider sums of a three-measurement sliding window
    sum_count = 0
    for i in range(2, len(measurements)):
        cur_sum = measurements[i-2] + measurements[i-1] + measurements[i]
        prev_sum = measurements[i-3] + measurements[i-2] + measurements[i-1]
        if cur_sum > prev_sum:
            sum_count += 1

    return sum_count
