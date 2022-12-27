import os


def p(data: str):
    print(data)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def rp(data: str):
    cls()
    p(data)
