from typing import List


def solve_part_1(input_data: str) -> int:
    # Split input into list of numbers and boards
    data = input_data.strip().split('\n')
    nums = list(map(int, data[0].split(',')))
    boards = [[int(x) for x in row.split()] for row in data[1:]]

    # Mark numbers on boards
    for num in nums:
        for board_index, board in enumerate(boards):
            squares_remaining = set(range(1, 26))
            for i, row in enumerate(board):
                for j, square in enumerate(row):
                    if square in nums:
                        squares_remaining.discard(square)

            if len(squares_remaining) == 0:
                score = sum(board[0]) * nums[-1]
                return score, board_index

    return None
