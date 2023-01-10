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


def solve_part_2(input_data):
    # Convert input string to a list of binary strings
    input_data = input_data.strip().split("\n")
    # Create a copy of the input data to use for filtering
    remaining_nums = input_data.copy()

    # Initialize variables to hold the rating values
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    # Iterate over each bit position
    for bit_position in range(len(input_data[0])):
        # Count the number of 1's and 0's in the current bit position
        num_ones = 0
        num_zeros = 0
        for num in remaining_nums:
            if num[bit_position] == "1":
                num_ones += 1
            else:
                num_zeros += 1

        # Determine the most/least common bit for the current position
        if num_ones > num_zeros:
            most_common_bit = "1"
            least_common_bit = "0"
        elif num_ones < num_zeros:
            most_common_bit = "0"
            least_common_bit = "1"
        else:
            most_common_bit = "1"
            least_common_bit = "0"

        # Filter the remaining numbers for the current bit position
        new_remaining_nums = []
        for num in remaining_nums:
            if num[bit_position] == most_common_bit:
                new_remaining_nums.append(num)
        remaining_nums = new_remaining_nums

        # If we have only one number remaining, it is the rating value
        if len(remaining_nums) == 1:
            # add the value to the corresponding rating
            oxygen_generator_rating = int(remaining_nums[0], 2)
            break

    # repeat the above loop for the co2_scrubber_rating
    remaining_nums = input_data.copy()
    for bit_position in range(len(input_data[0])):
        # Count the number of 1's and 0's in the current bit position
        num_ones = 0
        num_zeros = 0
        for num in remaining_nums:
            if num[bit_position] == "1":
                num_ones += 1
            else:
                num_zeros += 1

        # Determine the most/least common bit for the current position
        if num_ones > num_zeros:
            most_common_bit = "1"
            least_common_bit = "0"
        elif num_ones < num_zeros:
            most_common_bit = "0"
            least_common_bit = "1"
        else:
            most_common_bit = "1"
            least_common_bit = "0"

        # Filter the remaining numbers for the current bit position
        new_remaining_nums = []
        for num in remaining_nums:
            if num[bit_position] == least_common_bit:
                new_remaining_nums.append(num)
        remaining_nums = new_remaining_nums

        # If we have only one number remaining, it is the rating value
        if len(remaining_nums) == 1:
            co2_scrubber_rating = int(remaining_nums[0], 2)
            break

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating
