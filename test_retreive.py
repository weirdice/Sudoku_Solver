"""Script used for testing out getting puzzles from csv"""

import random

import pandas as pd

df = pd.read_csv(r"Sudoku_Solver/data_files/sudoku_data_updated.csv")
MAX_INDEX = df["puzzle"].count()
RandomIndex = random.randint(0, MAX_INDEX)
RandomPuzzle = df["puzzle"][RandomIndex]
RandomPuzzle = [*RandomPuzzle]

print(MAX_INDEX)
print(RandomIndex)
print(RandomPuzzle)
TransformedPuzzle = []
for i in range(0, 80, 9):
    TransformedPuzzle.append(RandomPuzzle[i : i + 9])

print(TransformedPuzzle)
