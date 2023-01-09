from Util import Coor, Direction, DirectionException


class Grid:
    def __init__(self, x_size=1, y_size=1):
        self.grid = [["" for _ in range(x_size)] for _ in range(y_size)]
        self.__x_offset__ = 0
        self.__y_offset__ = 0
        self.width = x_size
        self.height = y_size

    def add_at_index(self, coor: Coor, item) -> None:
        if not self.__has_coor__(coor):
            self.__extend_grid__(coor)
        self.grid[coor.y][coor.x] = item

    def __has_coor__(self, coor: Coor) -> bool:
        return coor.y < len(self.grid) - self.__y_offset__ and coor.y > 0 - self.__y_offset__ and coor.x < len(self.grid[coor.y]) - self.__x_offset__ and coor.x > 0 - self.__x_offset__

    def __extend_grid__(self, for_coor: Coor) -> None:
        cur_height = len(self.grid)
        cur_width = len(self.grid[0])

    def __extend_x__(self, amount: int, direction: Direction) -> None:
        extend_with = ["" for _ in range(amount)]
        if direction == Direction.LEFT:
            for y in range(len(self.grid)):
                self.grid[y] = extend_with + self.grid[y]
        elif direction == Direction.RIGHT:
            for y in range(len(self.grid)):
                self.grid[y].extend(extend_with)
        else:
            raise DirectionException(
                allowed_directions=[Direction.LEFT, Direction.RIGHT])
        self.width = len(self.grid[0])

    def __extend_y__(self, amount: int, direction: Direction) -> None:
        extend_with = [["" for _ in range(self.width)] for _ in range(amount)]
        if direction == Direction.UP:
            self.grid = extend_with + self.grid
        elif direction == Direction.DOWN:
            self.grid.extend(extend_with)
        else:
            raise DirectionException(
                allowed_directions=[Direction.UP, Direction.DOWN])

    def print(self):
        grid = [[" " if self.grid[y][x] == "" else self.grid[y][x] for x in range(
            len(self.grid[y]))] for y in range(len(self.grid))]
        [print(''.join(grid[y])) for y in range(len(grid))]
