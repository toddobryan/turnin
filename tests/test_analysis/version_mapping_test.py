from test_analysis import VersionMapping

vm1 = VersionMapping.parse("13,E,D,B,C,A")
vm2 = VersionMapping.parse("1,A,B,C,D,E")

def test_number():
    assert vm1.number == 13
    assert vm2.number == 1

def test_answer_indexes():
    assert vm1.answer_indexes == [4, 3, 1, 2, 0]
    assert vm2.answer_indexes == [0, 1, 2, 3, 4]

def test_letter_for_version():
    assert [vm1.letter_for_version(l) for l in "ABCDE"] == ["E", "D", "B", "C", "A"]
    assert [vm2.letter_for_version(l) for l in "ABCDE"] == ["A", "B", "C", "D", "E"]

def test_letters_for_version():
    assert [vm1.letters_for_version(l) for l in ["AC", "BE", "AD"]] == ["BE", "AD", "CE"]
    assert [vm2.letters_for_version(l) for l in ["AC", "BE", "AD"]] == ["AC", "BE", "AD"]

