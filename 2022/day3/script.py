import sys, os
sys.path.append(os.path.abspath(__file__ + "/../../../common"))

from Loader import get_data

data = get_data(2022, 3)
lines = data.strip().split("\n")


priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def run1():
    priority = 0
    for line in lines:
        comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
        for char in comp1:
            if char in comp2:
                priority += priorities.index(char)
                break
    print(priority)


def run2():
    priority = 0
    for i in range(0, len(lines), 3):
        r1, r2, r3 = lines[i:i+3]
        for char in r1:
            if char in r2 and char in r3:
                priority += priorities.index(char)
                break
    print(priority)


if __name__ == "__main__":
    run1()
    run2()
