from fractions import Fraction
from typing import List
from pathlib import Path

type VersionToQuestionToVersionMapping = dict[int, dict[str, VersionMapping]]

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def index_to_letter(index: int) -> str:
    return ALPH[index]

def letter_to_index(letter: str) -> int:
    assert len(letter) == 1
    return ALPH.index(letter)

class Answer:
    index: int
    text: str
    question: 'Question'

    def to_md(self, number: int, versions: VersionToQuestionToVersionMapping) -> str:
        spaces = " " * (len(str(number)) + 4)
        if self.text.startswith("```"):
            text = "\n" + self.text
        else:
            text = self.text
        text = text.replace("\n", f"\n{spaces}")
        return f"{spaces}* {(self.letters_by_version(versions))}. {text}"

    def letters_by_version(self, versions: VersionToQuestionToVersionMapping) -> str:
        letter_versions = []
        for v in versions:
            letter = versions[v][self.question.name].letter_for_version(index_to_letter(self.index))
            letter_versions.append(f"v{v}={letter}")
        return ",".join(letter_versions)

    def __init__(self, index: int, text: str, question: 'Question'):
        self.index = index
        self.text = text
        self.question = question

    def __str__(self):
        return f"{index_to_letter(self.index)}. {self.text}"

class Question:
    name: str
    text: str
    correct: dict[str, float]
    explanation: str
    answers: List[Answer]

    def to_md(self, number: int, versions: VersionToQuestionToVersionMapping) -> str:
        spaces = " " * (len(str(number)) + 2)
        text = self.text.replace("\n", f"\n{spaces}")
        numbers =  f"{number}. ({self.name}, {self.numbers_by_version(versions)}) "
        correct =  f"Correct: {self.correct_by_version(versions)}"
        answers = "\n".join([a.to_md(number, versions) for a in self.answers])
        md = f"{numbers}{correct}\\\n{spaces}{text}\n{answers}"
        return md

    def numbers_by_version(self, versions: VersionToQuestionToVersionMapping) -> str:
        numbers = []
        for v in versions:
            numbers.append(f"v{v}={versions[v][self.name].number}")
        return ", ".join(numbers)

    def correct_by_version(self, versions: VersionToQuestionToVersionMapping) -> str:
        correct_answers = []
        for v in versions:
            correct_this_version = []
            for letters, points in self.correct.items():
                pts = "" if points == 1 else f"={Fraction(points)}"
                letters_this_version = versions[v][self.name].letters_for_version(letters)
                correct_this_version.append(f"{letters_this_version}{pts}")
            correct_as_str = f"v{v}: {",".join(correct_this_version)}"
            correct_answers.append(correct_as_str)
        return "; ".join(correct_answers)


    def __init__(self, name: str, text: str, correct: dict[str, float], explanation: str = ""):
        self.name = name
        self.text = text
        self.correct = correct
        self.explanation = explanation
        self.answers = []

    def __str__(self):
        s = f"({self.name}) {self.text}\n"
        for a in self.answers:
            s += f"  {index_to_letter(a.index)} {a.text}\n"
        return s

    @staticmethod
    def parse(q_dump: str) -> 'Question':
        parts = q_dump.split("\n@\n")
        name_and_correct, text = parts[0].split("\n", 1)
        explanation = parts[-1]
        name, correct = Question.parse_name_and_correct(name_and_correct)
        question = Question(name, text, correct, explanation)
        answers = [Answer(i, text, question) for i, text in enumerate(parts[1:-1])]
        question.answers = answers
        return question

    @staticmethod
    def parse_name_and_correct(name_comma_correct: str) -> tuple[str, dict[str, float]]:
        name, corrects = name_comma_correct.split(",", 1)
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
        return name, correct_points

class VersionMapping:
    number: int
    answer_indexes: List[int]

    def __init__(self, number: int, answer_indexes: List[int]):
        self.number = number
        self.answer_indexes = answer_indexes

    def letters_for_version(self, letters: str) -> str:
        version_letters = [self.letter_for_version(l) for l in letters]
        version_letters.sort()
        return "".join(version_letters)

    def letter_for_version(self, letter: str) -> str:
        return index_to_letter(self.answer_indexes[letter_to_index(letter)])

    def canonical_letter_for_version(self, letter: str) -> str:
        return index_to_letter(self.answer_indexes[letter_to_index(letter)])

    def canonical_letters_for_version(self, letters: str) -> str:
        canonical_letters = [self.canonical_letter_for_version(l) for l in letters]
        canonical_letters.sort()
        return "".join(canonical_letters)

    @staticmethod
    def parse(line: str) -> 'VersionMapping':
        number, letters = line.split(",", 1)
        answer_indexes = [letter_to_index(l) for l in letters.split(",")]
        return VersionMapping(int(number), answer_indexes)

class QuestionSet:
    questions: List[Question]
    # map from version number to map of question name to version mapping
    versions: VersionToQuestionToVersionMapping

    def __init__(self, questions: List[Question], versions: dict[int, dict[str, VersionMapping]]):
        self.questions = questions
        self.versions = versions

    def get_answers(self, version, letter):
        return self.versions[version][letter].answer_indexes[ALPH.index(letter)]

    def to_md(self):
        mds = [q.to_md(i + 1, self.versions) for i, q in enumerate(self.questions)]
        return "\n\n".join(mds)

    @staticmethod
    def parse(question_dump: Path, question_correlation: Path, num_versions: int) -> 'QuestionSet':
        questions = parse_question_dump(question_dump)
        versions = parse_question_correlation(question_correlation, num_versions, questions)
        return QuestionSet(questions, versions)


def parse_question_dump(question_dump: Path) -> List[Question]:
    q_parts = question_dump.read_text().strip().split("\n@@")
    questions = [Question.parse(q) for q in q_parts]
    return questions

# question_correlation should be of the form
def parse_question_correlation(
        question_correlation: Path,
        num_versions: int,
        questions: List[Question],
) -> dict[int, dict[str, VersionMapping]]:
    all_lines = question_correlation.read_text().split("\n")
    lines = [line for line in all_lines if line.strip()]
    assert len(lines) == len(questions) * (num_versions + 1)
    versions: dict[int, dict[str, VersionMapping]] = {}
    for version_num in range(1, num_versions + 1):
        versions[version_num] = {}
    for i in range(0, len(lines), num_versions + 1):
        name = lines[i].strip()
        for version_num in range(1, num_versions + 1):
            versions[version_num][name] = VersionMapping.parse(lines[i + version_num])
    return versions

