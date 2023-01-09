from ..input import get_input


def solve_part_1(input_data: str) -> int:
    # Split the input data into a list of strings
    lines = input_data.strip().split("\n")

    # Convert the strings to integers and compute the fuel requirements
    fuel_requirements = [int(x) // 3 - 2 for x in lines]

    # Return the sum of the fuel requirements
    return sum(fuel_requirements)


def solve_part_2(input_data: str) -> int:
    # Split the input data into a list of strings
    lines = input_data.strip().split("\n")

    # Convert the strings to integers and compute the fuel requirements
    fuel_requirements = [int(x) // 3 - 2 for x in lines]

    # Recursively compute the additional fuel requirements
    total_fuel_requirement = 0
    for fuel in fuel_requirements:
        while fuel > 0:
            total_fuel_requirement += fuel
            fuel = fuel // 3 - 2

    # Return the total fuel requirement
    return total_fuel_requirement


if __name__ == "__main__":
    input = get_input(2021, 1)
    solve_part_1(input)
    solve_part_2(input)
