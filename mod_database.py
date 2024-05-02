"""
module transforms data from kaggle into a form usable by main module.
download data from here: https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings?resource=download"""

import tkinter as tk
from pathlib import Path
from time import time
from tkinter import filedialog

import pandas as pd


def main() -> None:
    root = tk.Tk()
    root.withdraw()
    # start tkinter but hide window

    filepath = filedialog.askopenfilename()
    start_time = time()  # start timer after getting filepath
    data_folder = Path("data_files/")
    save_file = data_folder / "sudoku_data_updated.csv"
    # location to save modified data

    root.quit()
    # close tkinter

    # "Sudoku_Solver\data_files\sudoku_data.csv"
    try:
        data = pd.read_csv(filepath, dtype=str)
        data = data.drop(columns=["solution", "clues"])

        def clean(value: str) -> str:
            value = str(value).replace(".", "0")
            return value

        data["puzzle"] = data["puzzle"].apply(clean)
        data.to_csv(save_file, index=False)
        total_time = round(time() - start_time, 3)
        print(
            f"data updated! \n total time: {total_time} seconds \n example of data follows:"
        )
        print(data.head())
    except ValueError:
        print(
            f"Invalid file path received please download data from kaggle: \n https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings?resource=download"
        )


if __name__ == "__main__":
    main()
