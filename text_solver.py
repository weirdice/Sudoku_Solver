"""Module imports a random sudoku puzzle from the above dataset and solves it."""

# dataset used:
# https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings?resource=download


# imports
import random

import pandas as pd

TEST_PUZZLE = [
    [6, 0, 0, 0, 0, 8, 0, 4, 0],
    [0, 0, 0, 0, 4, 0, 8, 0, 0],
    [5, 0, 0, 2, 0, 7, 0, 0, 0],
    [0, 2, 0, 7, 0, 5, 6, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 1, 0, 3, 0, 7, 0, 0],
    [0, 4, 0, 8, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0],
]


def get_puzzle(data_frame, max_index: int) -> list:
    """
    selects and returns a random sudoku puzzle from the "puzzle" column of the linked data frame
    """
    rand_index = random.randint(0, max_index)
    rand_puzzle = data_frame["puzzle"][rand_index]
    rand_puzzle = [int(x) for x in [*rand_puzzle]]
    transformed_puzzle = []
    for i in range(0, 80, 9):
        transformed_puzzle.append(rand_puzzle[i : i + 9])
    return transformed_puzzle


def solve_sudoku(puzzle, pos) -> bool:
    """
    Uses recursion to search for a solution to the puzzle given.get_puzzle
    Assumes that all spaces before position x,y have been filled
    """
    x, y = get_next_pos(puzzle, pos)
    # check for completed puzzle
    if x == 9:
        return True

    # test all digits in current spot
    for i in range(1, 10):
        if test(puzzle, [x, y], i):
            puzzle[x][y] = i
            if solve_sudoku(puzzle, [x, y]):
                return True
            puzzle[x][y] = 0
    return False


def get_next_pos(puzzle, pos) -> list:
    """
    Assumes puzzle is being solved from top left to bottom right.
    Given the current pos returns the next empty position.
    If no empty positions are found will return [9,0]
    """
    start_x, start_y = pos
    i = 9 * start_x + start_y
    while i < 81:
        if puzzle[i // 9][i % 9] == 0:
            break
        i += 1
    return [i // 9, i % 9]


def test(puzzle, pos, i) -> bool:
    """
    puzzle is current state of puzzle with 0 for unfilled rows
    pos is two coordinates for new digit
    i is digit to test in new position
    return true if i is not found in the row column or box
    """
    x, y = pos

    # get values from 3x3 box that includes pos
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    box = []
    rows = puzzle[start_x : start_x + 3]
    for column in rows:
        box += column[start_y : start_y + 3]

    # get column x
    column = []
    for row in puzzle:
        column.append(row[y])

    # get row
    row = puzzle[x]
    return not (i in box or i in column or i in row)


def string_puzzle(puzzle) -> str:
    """
    Takes a sudoku puzzle as a list of lists and converts it to a string to be printed out
    Formats by line and includes | and - to make borders between the 3x3 boxes
    """
    message = ""
    for i_row, row in enumerate(puzzle):
        if i_row % 3 == 0:
            message += "\n-------------------------------"
        message += "\n| "
        for i_col, item in enumerate(row):
            message += f"{item}"
            if i_col == 8:
                message += " |"
            elif i_col % 3 == 2:
                message += " | "
            else:
                message += ", "
    message += "\n-------------------------------"
    return message


def main():
    """Imports puzzle data and solves random puzzle"""
    df = pd.read_csv(r"data_files/sudoku_data_updated.csv")
    max_index = df["puzzle"].count()
    rand_puzzle = get_puzzle(df, max_index)

    print(string_puzzle(rand_puzzle))
    this_puzzle = []
    # create a true copy of puzzle
    for row in rand_puzzle:
        this_puzzle.append(row[:])
    # solve puzzle
    if solve_sudoku(this_puzzle, [0, 0]):
        print(string_puzzle(this_puzzle))
    else:
        print("This puzzle could not be solved")


if __name__ == "__main__":
    main()
