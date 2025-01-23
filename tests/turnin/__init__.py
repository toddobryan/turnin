import shutil
from importlib import resources as impres
from pathlib import Path
from typing import cast

import resources

HOME_FOLDERS = "home_folders"
STUDENT_LOGINS = ["student1", "student2", "student3"]

def start_from_scratch():
    home_folders = impres.files(resources) / HOME_FOLDERS
    for directory in home_folders.iterdir():
        directory: Path
        if directory.is_dir():
            shutil.rmtree(directory)
    for student_login in STUDENT_LOGINS:
        student_folder = cast(Path, home_folders / student_login)
        student_folder.mkdir(parents=True)


