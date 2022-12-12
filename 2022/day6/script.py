with open("./data") as f:
    line = f.read()


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
