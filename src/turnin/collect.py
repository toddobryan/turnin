from argparse import ArgumentParser
import pandas as pd
import pathlib
import shutil

ASSIGNMENTS_FOLDER = pathlib.Path("/") / "home" / "toddobryan" / "assignments"
TURNIN = "turnin"

def arg_parser():
    parser = ArgumentParser(prog="collect", description="grab all files from student turnin folders")
    parser.add_argument("period", help="which class to collect")
    parser.add_argument("filename", help="file to collect")
    return parser

def collect(period: str, filename: str, missing: dict[str, list[str]]) -> dict[str, list[str]]:
    print(f"Collecting {filename} from {period}")
    assignment_name = pathlib.Path(filename).stem
    extension = pathlib.Path(filename).suffix
    ASSIGNMENTS_FOLDER.mkdir(exist_ok=True)
    assignment_folder = ASSIGNMENTS_FOLDER / assignment_name
    period_folder = assignment_folder / period
    period_folder.mkdir(parents=True, exist_ok=True)

    resources_folder = pathlib.Path(__file__).parent / "resources"

    df = pd.read_csv(resources_folder / f"{period}.csv", names=["login", "last", "first", "nick"])
    logins = df["login"].tolist()
    for login in logins:
        student_folder = pathlib.Path("/") / "home" / login / TURNIN
        student_assignment = student_folder / filename
        if student_assignment.exists():
            shutil.copy2(student_assignment, assignment_folder / period / f"{login}.{extension}")
        else:
            if login not in missing:
                missing[login] = []
            missing[login].append(assignment_name)
    return missing

if __name__ == "__main__":
    missing = {}
    for period in ["r2", "r3", "r4", "w1", "w3"]:
        for assignment in [
            "image-exercises.rkt",
            "writing-functions.rkt",
            "project1.rkt",
            "more-design.rkt",
            "boolean-functions.rkt",
            "more-math.rkt",
            "conditional-functions.rkt",
            "road-trip.rkt",
        ]:
            missing = collect(period, assignment, missing)
    for login, assignments in missing.items():
        print(f"{login}: {", ".join(assignments)}")