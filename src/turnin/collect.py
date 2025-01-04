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

def main():
    parser = arg_parser()
    args = parser.parse_args()

    # assignment_name = pathlib.Path(args.filename).stem
    # extension = pathlib.Path(args.filename).suffix
    # ASSIGNMENTS_FOLDER.mkdir(exist_ok=True)
    # assignment_folder = ASSIGNMENTS_FOLDER / assignment_name
    # period_folder = assignment_folder / args.period
    # period_folder.mkdir(parents=True, exist_ok=True)

    resources_folder = pathlib.Path(__file__).parent / "resources"

    df = pd.read_csv(resources_folder / f"{args.period}.csv", names=["login", "last", "first", "nick"])
    logins = df["login"].tolist()
    for login in logins:
        print(login)
        # student_folder = pathlib.Path("/") / "home" / login / TURNIN
        # student_assignment = student_folder / args.filename
        # if student_assignment.exists():
        #     shutil.copy2(student_assignment, assignment_folder / f"{login}.{extension}")
        # else:
        #     print(f"{login} is missing {args.filename}")

if __name__ == "__main__":
    main()
