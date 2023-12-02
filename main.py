import argparse
import importlib
import importlib.util
import time
import os
from input import get_input
from datetime import datetime


def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="the year of the AOC challenge")
    parser.add_argument("day", type=int, help="the day of the AOC challenge")
    args = parser.parse_args()

    try:
        # Create a module spec for the specified year and day
        module_name = f"{args.year}/day{args.day}"
        module_path = os.path.join(os.getcwd(), f"{module_name}.py")
        module_spec = importlib.util.spec_from_file_location(
            module_name, module_path)

        # Create a module from the spec
        module = importlib.util.module_from_spec(module_spec)

        # Load the module into memory
        module_spec.loader.exec_module(module)
    except:
        if not str(args.year) in os.listdir(os.getcwd()):
            os.makedirs(str(args.year))
        if not f"day{args.day}.py" in os.listdir(os.path.join(os.getcwd(), str(args.year))):
            with open(os.path.join(os.getcwd(), str(args.year), f"day{args.day}.py"), "w+") as f:
                f.write(
                    f"def solve_part_1(input_data):\n    pass\n\ndef solve_part_2(input_data):\n    pass")
        print("Python script file created. Please fill in the functions.")

    # Get the input data for the specified day
    input_data = get_input(args.year, args.day)

    try:
        # Measure the elapsed time for solving Part 1
        start_time = datetime.now()
        result_1 = module.solve_part_1(input_data)
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        # Print the result and elapsed time for Part 1
        print(f"Part 1: {result_1}")
        print(f"Elapsed time: {elapsed_time} seconds")
    except Exception as e:
        print(e)

    try:
        # Measure the elapsed time for solving Part 2
        start_time = datetime.now()
        result_2 = module.solve_part_2(input_data)
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        # Print the result and elapsed time for Part 2
        print(f"Part 2: {result_2}")
        print(f"Elapsed time: {elapsed_time} seconds")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
