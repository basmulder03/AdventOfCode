from common.Loader import get_data

data = get_data(2022, 6)
line = data.strip()


def run1():
    for i in range(4, len(line)):
        chars = set(line[i-4:i])
        if len(chars) == 4:
            print(i)
            break


def run2():
    for i in range(14, len(line)):
        chars = set(line[i-14:i])
        if len(chars) == 14:
            print(i)
            break


if __name__ == "__main__":
    run1()
    run2()
