# advent of code 2021 day 1

def solve_part_1(input_data: str) -> int:
    # Parse the input data
    measurements = [int(x) for x in input_data.strip().split('\n')]
    # Count the number of times a depth measurement increases from the previous measurement
    count = sum([1 for measurement, prev in zip(
        measurements[1:], measurements[:-1]) if measurement > prev])
    return count


def solve_part_2(input_data: str) -> int:
    measurements = [int(x) for x in input_data.strip().split('\n')]
    # Consider sums of a three-measurement sliding window
    sum_count = sum([1 for a, b, c, d in zip(measurements[3:], measurements[2:-1],
                    measurements[1:-2], measurements[:-3]) if a+b+c > d+c+b])
    return sum_count
