import pandas as pd

# "Sudoku_Solver\data_files\sudoku_data.csv"
data = pd.read_csv(r"data_files/sudoku_data.csv", dtype=str)
data = data.drop(columns=["solution", "clues"])


def clean(value: str) -> str:
    value = str(value).replace(".", "0")
    return value


data["puzzle"] = data["puzzle"].apply(clean)
data.to_csv(r"data_files/sudoku_data_updated.csv", index=False)
print(data.head())
