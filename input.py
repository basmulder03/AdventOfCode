import os
import requests


def get_input(year: int, day: int) -> str:
    filename = f"input/{year}/day{day}.txt"
    cookie_filename = "session_cookie.txt"
    if os.path.exists(filename):
        # Read the input data from the file
        with open(filename, "r") as f:
            return f.read()
    else:
        # Read the session cookie from the file or prompt the user for a new one
        if os.path.exists(cookie_filename):
            with open(cookie_filename, "r") as f:
                session_cookie = f.read()
        else:
            session_cookie = input("Please enter your session cookie: ")
            with open(cookie_filename, "w+") as f:
                f.write(session_cookie)

        # Create a session and authenticate with the AOC website
        session = requests.Session()
        session.cookies.update({
            "session": session_cookie
        })
        response = session.get(
            f"https://adventofcode.com/{year}/day/{day}/input")
        if response.status_code == 403:
            # The cookie is no longer valid, prompt the user for a new one
            new_cookie = input(
                "Your session cookie is no longer valid. Please enter a new one: ")
            session.cookies.update({
                "session": new_cookie
            })
            response = session.get(
                f"https://adventofcode.com/{year}/day/{day}/input")
            # Save the new cookie to the file
            with open(cookie_filename, "w+") as f:
                f.write(new_cookie)
        response.raise_for_status()
        input_data = response.text

        current_dir = os.getcwd()
        for dir in filename.split("/")[:-1]:
            print(dir, current_dir)

            if not dir in os.listdir(current_dir):
                os.makedirs(os.path.join(current_dir, dir))
            current_dir = os.path.join(current_dir, dir)

        # Write the input data to the file
        with open(filename, "w+") as f:
            f.write(input_data)

        return input_data
