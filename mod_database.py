import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import pandas as pd


def main() -> None:

    root = tk.Tk()
    root.withdraw()
    # start tkinter but hide window

    filepath = filedialog.askopenfilename()
    data_folder = Path("data_files/")
    save_file = data_folder / "sudoku_data_updated.csv"
    # location to save modified data

    root.quit()
    # close tkinter

    # "Sudoku_Solver\data_files\sudoku_data.csv"
    data = pd.read_csv(filepath, dtype=str)
    data = data.drop(columns=["solution", "clues"])

    def clean(value: str) -> str:
        value = str(value).replace(".", "0")
        return value

    data["puzzle"] = data["puzzle"].apply(clean)
    data.to_csv(save_file, index=False)
    print(data.head())


if __name__ == "__main__":
    main()
