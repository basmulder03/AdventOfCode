from common.Loader import get_data

data = get_data(2022, 1)
lines = data.strip().split("\n")

def run1():
    elves = [0]
    for line in lines:
        if line == "":
            elves.append(0)
        else:
            elves[-1] += int(line)
    elves.sort(reverse=True)
    print(elves[0])


def run2():
    elves = [0]
    for line in lines:
        if line == "":
            elves.append(0)
        else:
            elves[-1] += int(line)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


if __name__ == "__main__":
    run1()
    run2()
