from enum import Enum


class Direction(Enum):
    NONE = 0
    UP = 1
    UPRIGHT = 2
    RIGHT = 3
    DOWNRIGHT = 4
    DOWN = 5
    DOWNLEFT = 6
    LEFT = 7
    UPLEFT = 8


class DirectionException(Exception):
    def __init__(self, message: str = "This direction is not allowed, you are only allowed the directions: {}", allowed_directions: list[Direction] = []):
        self.message = message.format(', '.join(allowed_directions))
        super().__init__(self.message)


class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def go_up(self, amount=1):
        self.y += amount

    def go_down(self, amount=1):
        self.y -= amount

    def go_right(self, amount=1):
        self.x += amount

    def go_left(self, amount=1):
        self.x -= amount

    def get_direction(self, other) -> Direction:
        if self.x == other.x and self.y == other.y:
            return Direction.NONE
        elif self.x == other.x:
            if self.y > other.y:
                return Direction.DOWN
            else:
                return Direction.UP
        elif self.y == other.y:
            if self.x > other.x:
                return Direction.LEFT
            else:
                return Direction.RIGHT
        else:
            if self.x > other.x and self.y > other.y:
                return Direction.DOWNLEFT
            elif self.x > other.x and self.y < other.y:
                return Direction.UPLEFT
            elif self.x < other.x and self.y > other.y:
                return Direction.DOWNRIGHT
            elif self.x < other.x and self.y < other.y:
                return Direction.UPRIGHT
            else:
                print("Forgot a combination")
                return Direction.NONE

    def move_coor(self, coor):
        self.x += coor.x
        self.y += coor.y
        return self

    def copy(self):
        return Coor(self.x, self.y)
