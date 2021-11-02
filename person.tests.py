import unittest

from person import Person
from person import PersonRegister

class PersonTest(unittest.TestCase):
    def test_when_creating_person_personnumber_should_be_set(self):
        target = Person("19720803-0000")

        self.assertEqual("19720803-0000", target.getPersonalNumber())


class PersonRegisterTest(unittest.TestCase):
    def test_when_fetching_person_correct_person_should_be_fetched(self):
        p1 = Person("19720803-0000")
        p1.setName("Stefan")
        p2 = Person("19720101-0000")
        p2.setName("Kalle")

        target = PersonRegister()
        target.add(p1)
        target.add(p2)

        self.assertEqual(p1, target.getPerson("19720803-0000"))


if __name__ == "__main__":
    unittest.main()