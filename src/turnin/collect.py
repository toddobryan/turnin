import glob
import os
from argparse import ArgumentParser
import pandas as pd
from pathlib import Path
import pathlib
import shutil

from . import TURNIN, date_tag, datetime_tag, get_current_user, ALL_PERIODS, ALL_ASSIGNMENTS

collect_parser = ArgumentParser(prog="collect", description="collect student work")
collect_parser.add_argument("period")
collect_parser.add_argument("filename")


def turnin_folder(login: str) -> Path:
    return Path("/home") / login / TURNIN

def collect(
        period: str,
        filename: str,
        missing: dict[str, list[str]] = None,
        assignments_folder: str = None,
) -> dict[str, list[str]]:
    if not missing:
        missing = {}
    if not assignments_folder:
        assignments_folder = Path("/home") / get_current_user() / "assignments"
    print(f"Collecting {filename} from {period}")
    print(f"assignments folder: {assignments_folder}")
    assignment_name = pathlib.Path(filename).stem
    extension = pathlib.Path(filename).suffix
    assignments_folder.mkdir(exist_ok=True)
    assignment_folder = assignments_folder / assignment_name
    period_folder = assignment_folder / period
    period_folder.mkdir(parents=True, exist_ok=True)

    resources_folder = pathlib.Path(__file__).parent / "resources"

    df = pd.read_csv(resources_folder / f"{period}.csv", names=["login", "last", "first", "nick"])
    logins = df["login"].tolist()
    for login in logins:
        home_folder = pathlib.Path("/") / "home" / login
        if not home_folder.exists():
            print(f"{login} has no home folder")
            continue

        collected_folder = turnin_folder(login) / "collected"
        collected_folder.mkdir(exist_ok=True)
        student_assignment = turnin_folder(login) / filename
        if student_assignment.exists():
            student_assignment_collected = collected_folder / f"{assignment_name}-{datetime_tag()}{extension}"
            shutil.copy2(student_assignment, assignment_folder / period / f"{login}{extension}")
            shutil.move(student_assignment, student_assignment_collected)
        else:
            previous_files = glob.glob(os.path.join(collected_folder, f"{assignment_name}*"))
            if previous_files:
                for file in previous_files:
                    name_with_date = Path(file).name
                    login_with_date = name_with_date.replace(assignment_name, login)
                    shutil.move(file, assignment_folder / period / login_with_date)
            else:
                if login not in missing:
                    missing[login] = []
                missing[login].append(assignment_name)
                missing_file = turnin_folder(login) / f"missing-{filename}"
                missing_file.touch()
                shutil.chown(missing_file, user=login, group=login)
        shutil.chown(collected_folder, user="root", group="root")
        os.chmod(collected_folder, 0o555)

    return missing

if __name__ == "__main__":
    missing = {}
    for period in ALL_PERIODS:
        for assignment in ALL_ASSIGNMENTS:
            missing = collect(period, assignment, missing=missing)
    for login, assignments in missing.items():
        print(f"{login}: {', '.join(assignments)}")