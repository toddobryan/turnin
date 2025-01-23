import os
from datetime import datetime, timezone
from pathlib import Path
import shutil

from .collect import turnin_folder

def chown_dash_r(path: Path, user: str, group: str):
    for dir_path, _, filenames in os.walk(path):
        shutil.chown(dir_path, user=user, group=group)
        for f in filenames:
            shutil.chown(os.path.join(dir_path, f), user=user, group=group)

def chmod_dash_r(path: Path, mode: int):
    for dir_path, _, filenames in os.walk(path):
        os.chmod(dir_path, mode)
        for f in filenames:
            os.chmod(os.path.join(dir_path, f), mode)

def put_student_work_in_turnin():
    student_work_folder = Path.home() / "StudentWork"
    for student_folder in student_work_folder.iterdir():
        if student_folder.is_dir():
            student_turnin_folder = turnin_folder(student_folder.name)
            student_turnin_folder.mkdir(parents=True, exist_ok=True)
            older_folder = student_turnin_folder / "older"
            older_folder.mkdir(exist_ok=True)
            for assignment in student_folder.iterdir():
                if assignment.is_file():
                    student_file = student_turnin_folder / assignment.name
                    print(f"Copying {student_folder.basename}/{assignment.name}} to turnin")
                    if student_file.exists():
                        stat = student_file.stat()
                        student_file_without_extension = student_file.basename.with_suffix("")
                        student_file_extension = student_file.suffix
                        m_time = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
                        m_time_str = m_time.strftime("%Y-%m-%d-%H-%M")
                        older_file = (older_folder /
                                      f"{student_file_without_extension}-{m_time_str}{student_file_extension}")
                        print(f"File already exists; moving to older/{older_file.basename}")
                        shutil.move(student_file, older_file)
                    shutil.copy2(assignment, student_turnin_folder / student_file)
