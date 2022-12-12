with open("./data") as f:
    lines = f.read().split("\n")


winning = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

drawing = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

losing = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def run1():
    current_points = 0
    for line in lines:
        opponent, you = line.split(" ")
        current_points += points[you]
        if winning[opponent] == you:
            current_points += 6
        elif drawing[opponent] == you:
            current_points += 3
    print(current_points)


def run2():
    current_points = 0
    for line in lines:
        opponent, needed_score = line.split(" ")
        if needed_score == 'X':
            you = losing[opponent]
        elif needed_score == 'Y':
            you = drawing[opponent]
            current_points += 3
        else:
            you = winning[opponent]
            current_points += 6
        current_points += points[you]
    print(current_points)


if __name__ == "__main__":
    run1()
    run2()
