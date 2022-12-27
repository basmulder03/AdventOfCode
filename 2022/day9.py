from common.Loader import get_data
from common.Util import Coor, Direction

data = get_data(2022, 9)


def parse(data: str):
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    lines = data.strip().split("\n")
    splitted_lines = [line.split(" ") for line in lines]
    return [(d, int(a)) for d, a in splitted_lines]


directions = {
    Direction.NONE: Coor(0, 0),
    Direction.UP: Coor(0, 1),
    Direction.UPRIGHT: Coor(1, 1),
    Direction.RIGHT: Coor(1, 0),
    Direction.DOWNRIGHT: Coor(1, -1),
    Direction.DOWN: Coor(0, -1),
    Direction.DOWNLEFT: Coor(-1, -1),
    Direction.LEFT: Coor(-1, 0),
    Direction.UPLEFT: Coor(-1, 1)
}


def coor_is_close(head: Coor, tail: Coor):
    tail_is_close = False
    for new_coor in directions.values():
        copycat = tail.copy()
        if copycat.move_coor(new_coor) == head:
            tail_is_close = True
            break
    return tail_is_close


def part1(data):
    actions = parse(data)
    visited = set()
    current_head_coors = Coor(0, 0)
    current_tail_coors = Coor(0, 0)

    visited.add(current_tail_coors)

    for direction, amount in actions:
        for _ in range(amount):
            if direction == 'U':
                current_head_coors.go_up()
            elif direction == 'D':
                current_head_coors.go_down()
            elif direction == 'R':
                current_head_coors.go_right()
            elif direction == 'L':
                current_head_coors.go_left()

            if not coor_is_close(current_head_coors, current_tail_coors):
                direction_to_move = current_tail_coors.get_direction(
                    current_head_coors)
                visited.add(current_tail_coors.move_coor(
                    directions[direction_to_move]))

    print(len(visited))


if __name__ == "__main__":
    part1(data)
