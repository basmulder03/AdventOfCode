from common.Loader import get_data
from common.Terminal import Color

data = get_data(2022, 8)


def parse():
    return [[int(tree) for tree in trees] for trees in data.strip().split("\n")]


def run1():
    forest = parse()
    visible = [[False for _ in range(len(forest[y]))]
               for y in range(len(forest))]

    for y in range(len(forest)):
        highest_from_left = -1
        highest_from_right = -1
        for x in range(len(forest[y])):
            if forest[y][x] > highest_from_left:
                visible[y][x] = True
                highest_from_left = forest[y][x]
            if forest[y][len(forest[y]) - x - 1] > highest_from_right:
                visible[y][len(forest[y]) - x - 1] = True
                highest_from_right = forest[y][len(forest[y]) - x - 1]
    for x in range(len(forest[y])):
        highest_from_top = -1
        highest_from_bottom = -1
        for y in range(len(forest)):
            if forest[y][x] > highest_from_top:
                visible[y][x] = True
                highest_from_top = forest[y][x]
            if forest[len(forest) - y - 1][x] > highest_from_bottom:
                visible[len(forest) - y - 1][x] = True
                highest_from_bottom = forest[len(forest) - y - 1][x]
    # [print(''.join([Color.BOLD + Color.GREEN + str(forest[y][x]) + Color.END if visible[y][x] else Color.RED + str(forest[y][x]) + Color.END for x in range(len(forest[y]))])) for y in range(len(forest))]
    print(sum([sum(y) for y in visible]))


def valid_index(list, index):
    return index >= 0 and index < len(list)


def run2():
    forest = parse()
    highscore = (-1, -1, -1, -1, -1)
    highscore_coors = (-1, -1)
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            current_height = forest[y][x]
            x1, x2, y1, y2 = True, True, True, True
            up, down, left, right = 0, 0, 0, 0
            while (x1 or x2 or y1 or y2):
                if x1 and not valid_index(forest[y], x + right + 1):
                    x1 = False
                if x2 and not valid_index(forest[y], x - left - 1):
                    x2 = False
                if y1 and not valid_index(forest, y - up - 1):
                    y1 = False
                if y2 and not valid_index(forest, y + down + 1):
                    y2 = False

                if x1:
                    right += 1
                    if forest[y][x + right] >= current_height:
                        x1 = False
                if x2:
                    left += 1
                    if forest[y][x - left] >= current_height:
                        x2 = False
                if y1:
                    up += 1
                    if forest[y - up][x] >= current_height:
                        y1 = False
                if y2:
                    down += 1
                    if forest[y + down][x] >= current_height:
                        y2 = False
                score = up * down * left * right
                if score > highscore[0]:
                    highscore = (score, x1, x2, y1, y2)
                    highscore_coors = (x, y)
    [print(''.join([Color.BOLD + Color.GREEN + str(forest[y][x]) + Color.END if x == highscore_coors[0] and y == highscore_coors[1] else Color.GREEN + str(forest[y][x]) + Color.END if (x == highscore_coors[0] and y < highscore_coors[1] and y > highscore_coors[1] - highscore[3]) or (x == highscore_coors[0] and y > highscore_coors[1] and y <
           highscore_coors[1] + highscore[4]) or (y == highscore_coors[1] and x > highscore_coors[0] and x < highscore_coors[0] + highscore[1]) or (y == highscore_coors[1] and x < highscore_coors[0] and x > highscore_coors[0] - highscore[2]) else Color.RED + str(forest[y][x]) + Color.END for x in range(len(forest[y]))])) for y in range(len(forest))]
    print(highscore[0])


if __name__ == "__main__":
    run1()
    run2()
