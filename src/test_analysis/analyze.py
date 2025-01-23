from pathlib import Path
import pandas as pd
import importlib.resources as impres

from . import resources


def last_two(path):
    return "/".join(Path(path).parts[-2:])

def v_num(version: str) -> int:
    if version in "AB":
        return "AB".index(version) + 1
    else:
        return 0

def clean_up():
    students_by_page = {}
    with open("resources/student_by_page.csv", "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            if line:
                page, login = line.split(",")
                period, _ = page.split("/")
                #print(period, login, page)
                students_by_page[page] = (login, period)

    df = pd.read_csv("resources/final.csv")
    df["input_path"] = df["input_path"].apply(last_two).apply(lambda x: x[0:-4]) # strip .jpg from end
    logins_and_periods = [students_by_page[ip] for ip in df["input_path"].tolist()]
    logins = [item[0] for item in logins_and_periods]
    periods = [item[1] for item in logins_and_periods]

    df["version"] = df["version"].apply(v_num)
    df.insert(loc=0, column="login", value=pd.Series(logins))
    df.insert(loc=1, column="period", value=pd.Series(periods))
    df.insert(loc=2, column="version_num", value=df["version"])

    df.drop(["input_path", "file_id", "score", "output_path", "version"], axis=1, inplace=True)
    df.to_csv("resources/final_cleaned.csv", index=False)

def create_question_correlation() -> (list[str], dict[str, dict[str, str]]):
    q_correlation_map = {}
    q_names = []
    groups = []
    corr_file = impres.files(resources) / "question_correlation.csv"
    with corr_file.open("r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            groups.append(lines[i:i+3])

    for group in groups:
        name, correct = group[0].split(",", 1)
        v1_num, v1_answers = group[1].split(",", 1)
        v2_num, v2_answers = group[2].split(",", 1)
        q_names.append(name)
        q_correlation_map[name] = {
            "correct": correct.split(","),
            1: {"number": int(v1_num), "answers": v1_answers.split(",")},
            2: {"number": int(v2_num), "answers": v2_answers.split(",")},
        }

    return q_names, q_correlation_map

def get_answers(student_answers, answers):
    def correlated_answer(letter):
        if letter in answers:
            return "ABCDE"[answers.index(letter)]
        else:
            return ""
    return "".join([correlated_answer(letter) for letter in student_answers])

# def calculate_score(student_row, version):
#     score = 0
#     for qn, qs in questions.items():
#         student_question_number = "Q%d" % qs[version]["number"]
#         student_answers = student_row[student_question_number]
#         answers = qs["correct"]
#         #print(student_answers, get_answers(student_answers, qs[version]["answers"]), answers)
#         poss_points = len(answers)
#         points_this_question = 0
#         for letter in get_answers(student_answers, qs[version]["answers"]):
#             if letter in answers:
#                 points_this_question += 1
#             else:
#                 points_this_question -= 1
#         score += max(0, points_this_question / poss_points)
#         #print(score)
#     return score

# def create_new_row(row):
#     login = row["login"]
#     period = row["period"]
#     version = int(row["version_num"])
#     print(login, version, calculate_score(row, 1), calculate_score(row, 2))

def correlate():
    with open("resources/final_cleaned.csv", "r") as file:
        df = pd.read_csv(file)
    df.fillna("", inplace=True)

    #correlated = pd.DataFrame()

    # for i in range(len(df)):
    #     row = df.iloc[i]
    #     create_new_row(row)

if __name__ == "__main__":
    correlate()
