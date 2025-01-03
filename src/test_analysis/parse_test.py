import lxml.etree as ET

import importlib.resources as impres
from typing import List

from . import resources

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Question:
    def __init__(self, name: str, text: str, answers=None):
        if answers is None:
            answers = []
        self.name: str = name
        self.text: str = text
        self.answers: [Answer] = answers

    def __str__(self):
        s = self.text + '\n'
        for i, a in enumerate(self.answers):
            s += f"  {ALPH[i + 1]}{a.correct_mark()} {str(a)}\n"
        return s

    def xml(self):
        question = ET.Element("question")
        question.set("name", self.name)
        text_element = ET.Element("text")
        text_element.text = self.text
        question.append(text_element)
        for a in self.answers:
            question.append(a.xml())
        return question

class Answer:
    def __init__(self, text, is_correct: bool = False):
        self.text: str = text
        self.is_correct: bool = is_correct

    def __str__(self):
        return self.text

    def xml(self):
        answer = ET.Element("answer")
        answer.text = self.text
        if self.is_correct:
            answer.set("isCorrect", "true")
        return answer

    def correct_mark(self) -> str:
        if self.is_correct:
            return "*"
        else:
            return ""


def read_test_ezml(input_file) -> ET.Element:
    with input_file.open("rt") as file:
        whole_file = file.read()

    root = ET.Element("test")
    questions = whole_file.split("\n@@")
    for q in questions:
        name, rest = q.split("\n", 1)
        text_and_answers = rest.split("\n@\n")
        question_text = text_and_answers[0]
        answers = text_and_answers[1:-1]
        correct = [ALPH.index(letter) for letter in map(lambda s: s.strip(), text_and_answers[-1].split(","))]
        answer_list = []
        for i, a in enumerate(answers):
            answer_list.append(Answer(a, i in correct))
        question = Question(name, question_text, answer_list)
        root.append(question.xml())

    return root

if __name__ == "__main__":
    __package__ = "test_analysis"
    read_test_ezml(impres.files(resources) / "apcsp-final.ezml")

