from pathlib import Path
from typing import cast

from .questions import Question, Answer, QuestionSet, VersionToQuestionToVersionMapping
from .analyze import create_question_correlation
from . import resources

from importlib import resources as impres

ALPH_CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class StudentAnswers:
    login: str
    period: str
    version: int
    answers: list[str]
    score: int
    canonical_answers: list[str]

    def __init__(self, login, period, version, answers, canonical_answers: list[str]):
        self.login = login
        self.period = period
        self.version = version
        self.answers = answers
        self.canonical_answers = canonical_answers

    @staticmethod
    def parse(line: str, questions: list[Question], versions: VersionToQuestionToVersionMapping):
        parts = line.split(",", 3)
        login = parts[0]
        period = parts[1]
        version = int(parts[2])
        answers = parts[3].strip().split(",")
        canonical_answers = []
        for question in questions:
            index = versions[version][question.name].number - 1
            canonical_answers.append(versions[version][question.name].canonical_letters_for_version(answers[index]))
        return StudentAnswers(login, period, version, answers, canonical_answers)

    def __str__(self):
        return f"{self.login}, {self.period}, {self.version}\n{self.answers}\n{self.canonical_answers}"


def parse_student_answers(qset: QuestionSet) -> list[StudentAnswers]:
    student_answer_file = impres.files(resources) / "final_cleaned.csv"
    with student_answer_file.open("r") as f:
        lines = [line for line in f.readlines() if line.strip()][1:]
    return [StudentAnswers.parse(line, qset.questions, qset.versions) for line in lines]


def parse_questions(file) -> list[Question]:
    questions = []
    with open(file, "r") as f:
        q_parts = f.read().split("\n@@")
        for q in q_parts:
            parts = q.split("\n@\n")
            name_and_correct, text = parts[0].split("\n", 1)
            name, corrects = name_and_correct.split(",", 1)
            corrects = corrects.split(",")
            correct_points = {}
            if len(corrects) == 1 and "=" not in corrects[0]:
                correct_points[corrects[0]] = 1
            else:
                for correct in corrects:
                    if "=" in correct:
                        correct_name, points = correct.split("=")
                        correct_points[correct_name] = float(points)
                    else:
                        correct_points[correct] = 1
            answers = []
            question = Question(name, text, correct_points, answers)
            for i, answer in enumerate(parts[1:-1]):
                answers.append(Answer(i, answer, question))

            question.answers = answers
            questions.append(question)

    return questions

def answer_to_md(number: int, answer: Answer) -> str:
    q = answer.question
    v1_answers = q.get_answers(1, answer.letter)
    v2_answers = q.get_answers(2, answer.letter)
    spaces = " " * (len(str(number)) + 4)
    if answer.text.startswith("```"):
        text = "\n" + answer.text
    else:
        text = answer.text
    text = text.replace("\n", f"\n{spaces}")
    return f"""{spaces}* (v1={v1_answers}, v2={v2_answers}).  {text}"""


def analyze_student(sa: StudentAnswers, qset: QuestionSet):
    print(sa.login, sa.version)
    for i, q in enumerate(qset.questions[0:5]):
        print(q.name, q.correct)
        corresponding_question = qset.versions[sa.version][q.name].number
        print(corresponding_question, sa.answers[corresponding_question - 1], sa.canonical_answers[i])


def print_score_and_wrong_answers(qset: QuestionSet):
    student_answers = parse_student_answers(qset)
    analyze_student(student_answers[0], qset)

    # for sa in student_answers[0:1]:
    #     print(sa)
    #     score = 0
    #     wrongs = []
    #     amounts = []
    #     for i, q in enumerate(qset.questions):
    #         print(q.name, q.correct)
    #         plus = q.correct.get(sa.canonical_answers[i], 0)
    #         print(sa.answers[qset.versions[sa.version][q.name].number - 1], sa.canonical_answers[i])
    #         if plus != 1:
    #             number = qset.versions[sa.version][q.name].number
    #             amount = " -1/2" if plus == 0.5 else ""
    #             wrongs.append(q.name)
    #             amounts.append(amount)
    #         score += plus
    #     sa.score = round(score * 2)
    #     wrongs_and_amounts = [(w, a) for (w, a) in zip(wrongs, amounts)]
    #     wrongs_and_amounts.sort(key=lambda x: x[0])
    #     wrongs = [f"{w}{a}" for w, a in wrongs_and_amounts]
    #     print(f"{sa.login}, {sa.version}, {round(score * 2)}, ({", ".join(wrongs)})")


def main():
    question_dump = cast(Path, impres.files(resources) / "apcsp-final.md")
    question_corr = cast(Path, impres.files(resources) / "question_correlation.csv")
    qs = QuestionSet.parse(question_dump, question_corr, 2)
    print_score_and_wrong_answers(qs)

    #for q in qs.questions:


    # _, q_correlation_map = create_question_correlation()
    # qs = parse_questions(impres.files(resources) / "apcsp-final.md")
    # correlated_qs = []
    # for q in qs:
    #     q.v1_number = q_correlation_map[q.name][1]["number"]
    #     q.v2_number = q_correlation_map[q.name][2]["number"]
    #     q.v1_answers = q_correlation_map[q.name][1]["answers"]
    #     q.v2_answers = q_correlation_map[q.name][2]["answers"]
    #     correlated_qs.append(q)
    #
    # student_answers = parse_student_answers(correlated_qs)
    # for sa in student_answers:
    #     score = 0
    #     for i, q in enumerate(correlated_qs):
    #         plus = q.correct.get(sa.canonical_answers[i], 0)
    #         score += plus
    #     sa.score = round(score * 2)
    #     print(f"{sa.login}, {sa.version}, {round(score * 2)}")

    # student_answers.sort(key=lambda x: x.score, reverse=True)
    # for i, q in enumerate(correlated_qs):
    #     q.full_credit = 0
    #     q.partial_credit = 0
    #     q.number_answered = [0 for _ in range(len(q.answers))]
    #     for sa in student_answers:
    #         plus = q.correct.get(sa.canonical_answers[i], 0)
    #         if plus == 1:
    #             q.full_credit += 1
    #         elif plus > 0:
    #             q.partial_credit += 1
    #         for letter in sa.canonical_answers[i]:
    #             q.number_answered[ALPH_CAP.index(letter)] += 1



    #print("\n".join([to_md(i + 1, q) for i, q in enumerate(qs)]))

if __name__ == "__main__":
    main()