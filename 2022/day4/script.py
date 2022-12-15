import sys, os
sys.path.append(os.path.abspath(__file__ + "/../../../common"))

from Loader import get_data

data = get_data(2022, 4)
lines = data.strip().split("\n")


def run1():
    contains = 0
    for line in lines:
        r1, r2 = line.split(",")
        range1 = r1.split("-")
        range2 = r2.split("-")
        if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
            contains += 1
        elif int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1]):
            contains += 1
    print(contains)


def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]


def run2():
    contains = 0
    for line in lines:
        r1, r2 = line.split(",")
        range1, range2 = r1.split("-"), r2.split("-")
        x = range(int(range1[0]), int(range1[1])+1)
        y = range(int(range2[0]), int(range2[1])+1)
        if len(intersection(x, y)) > 0:
            contains += 1
    print(contains)


if __name__ == "__main__":
    run1()
    run2()
