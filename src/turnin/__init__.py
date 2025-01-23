from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

from .collect import collect

turnin_parser = ArgumentParser(prog="turnin", description="handle turnin procedures")
turnin_parser.add_argument("command", choices=["collect", "move_to_turnin"])
turnin_parser.add_argument("-e", "--environment", choices=["prod", "test"], default="test")

subparsers = turnin_parser.add_subparsers(dest="command")
collect_parser = subparsers.add_parser("collect", description="collect student work")
collect_parser.add_argument("period")
collect_parser.add_argument("assignment_file")
collect_parser.add_argument("directory")

move_to_turnin_parser = subparsers.add_parser("move_to_turnin", description="move student work into turnin folder")
move_to_turnin_parser.add_argument("from_directory")


ASSIGNMENTS_FOLDER = Path("/") / "home" / "toddobryan" / "assignments"
TURNIN = "turnin"
ALL_ASSIGNMENTS = [
    "image-exercises.rkt",
    "writing-functions.rkt",
    "project1.rkt",
    "more-design.rkt",
    "boolean-functions.rkt",
    "more-math.rkt",
    "conditional-functions.rkt",
    "road-trip.rkt",
]
ALL_PERIODS = ["r2", "r3", "r4", "w1", "w3"]

def datetime_tag() -> str:
    """Returns current datetime in the form YYYY-MM-DD-HH-MM"""
    return datetime.now().strftime("%Y-%m-%d-%H-%M")

if __name__ == "__main__":
    turnin_args = turnin_parser.parse_args()
    missing = collect(periods, assignments)
    for login, assignments in missing.items():
        print(f"{login}: {", ".join(assignments)}")
    print("\n  Don't forget to chown assignments.")

