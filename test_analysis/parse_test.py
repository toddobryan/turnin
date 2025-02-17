import lxml.etree as ET

import importlib.resources as impres

from . import resources

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

