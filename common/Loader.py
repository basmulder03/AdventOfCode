import requests


user_token = "53616c7465645f5fe4959493ab69ecf4df895b516cf6ab6123d4c08cec4ebf5331c2b51f826640bad4f24bcec98e94c3029aee4a9cbbbc21c009fe00d02f168a"

cookies = {'session': user_token}


def get_data(year: int, day: int):
    r = requests.get("https://adventofcode.com/{}/day/{}/input".format(year, day), cookies=cookies)
    return r.text