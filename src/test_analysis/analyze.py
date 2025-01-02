from pathlib import Path
import pandas as pd
import importlib.resources

def last_two(path):
    return "/".join(Path(path).parts[-2:])

def clean_up():
    df = pd.read_csv("resources/final.csv")
    df.drop(["file_id", "score", "output_path"], axis=1, inplace=True)
    df["input_path"] = df["input_path"].apply(last_two)
    df.to_csv("resources/final_cleaned.csv", index=False)

def correlate(answers):
    df = pd.read_csv(answers)
    grouped = df.groupby("version")
    print(grouped.groups)
    v1 = grouped.get_group("A")
    v2 = grouped.get_group("B")
    print("Version 1")
    print(v1)
    print("Version 2")
    print(v2)

if __name__ == "__main__":
    clean_up()
