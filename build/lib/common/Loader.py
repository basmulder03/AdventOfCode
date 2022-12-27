import requests


user_token = "53616c7465645f5f71ca72aadb0fa64c7eb0921ead1d348bc3946ec5f37222b075a3a289a495c616d4516471ba850e7a9cdac33bf39d641b8ccf307ea9d15af9"

cookies = {'session': user_token}


def get_data(year: int, day: int):
    r = requests.get(
        "https://adventofcode.com/{}/day/{}/input".format(year, day), cookies=cookies)
    return r.text
