def solve_part_1(input_data: str) -> int:
    # Parse the input
    binary_numbers = [x.strip() for x in input_data.strip().split('\n')]

    # Calculate the gamma rate
    gamma_rate = ''
    for i in range(len(binary_numbers[0])):
        ones = 0
        zeros = 0
        for number in binary_numbers:
            if number[i] == '0':
                zeros += 1
            elif number[i] == '1':
                ones += 1
        if ones > zeros:
            gamma_rate += '1'
        else:
            gamma_rate += '0'

    # Calculate the epsilon rate
    epsilon_rate = ''
    for i in range(len(binary_numbers[0])):
        ones = 0
        zeros = 0
        for number in binary_numbers:
            if number[i] == '0':
                zeros += 1
            elif number[i] == '1':
                ones += 1
        if ones < zeros:
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'

    # Calculate the power consumption
    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)
    power_consumption = gamma_rate_int * epsilon_rate_int
    return power_consumption


def solve_part_2(input_data: str) -> int:
    def calculate_life_support_rating(input_data: str) -> int:
        binary_numbers = input_data.strip().split('\n')
        oxygen_generator_rating = ''
        for i in range(len(binary_numbers[0])):
            ones = 0
            zeros = 0
            for number in binary_numbers:
                if number[i] == '0':
                    zeros += 1
                else:
                    ones += 1
            if ones > zeros:
                oxygen_generator_rating += '1'
            else:
                oxygen_generator_rating += '0'
        co2_scrubber_rating = ''
        for i in range(len(binary_numbers[0])):
            ones = 0
            zeros = 0
            for number in binary_numbers:
                if number[i] == '0':
                    zeros += 1
                else:
                    ones += 1
            if ones < zeros:
                co2_scrubber_rating += '0'
            else:
                co2_scrubber_rating += '1'
        return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

    return calculate_life_support_rating(input_data)
