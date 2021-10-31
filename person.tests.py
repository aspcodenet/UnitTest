import unittest

from person import Person
from person import PersonRegister

class PersonTest(unittest.TestCase):
    def test_when_creating_person_name_and_personnumber_should_be_set(self):
        target = Person("Stefan", "19720803-0000")

        self.assertEqual("Stefan", target.getName())
        self.assertEqual("19720803-0000", target.getPersonalNumber())


class PersonRegisterTest(unittest.TestCase):
    def test_when_fetching_person_correct_person_should_be_fetched(self):
        p1 = Person("Stefan", "19720803-0000")
        p2 = Person("Kalle", "19720101-0000")

        target = PersonRegister()
        target.add(p1)
        target.add(p2)

        self.assertEqual(p1, target.getPerson("19720803-0000"))


if __name__ == "__main__":
    unittest.main()