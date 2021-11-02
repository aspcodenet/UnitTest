import unittest

from person import Person
from person import PersonRegister

class PersonTest(unittest.TestCase):
    def test_when_creating_person_personnumber_should_be_set(self):
        target = Person("19720803-0000")
        persNr = target.getPersonalNumber()
        self.assertEqual("19720803-0000",persNr )

    def test_setname_should_change_name(self):
        target = Person("19720803-0000")
        target.setName("Stefan")
        vardet = target.getName()
        self.assertEqual("Stefan", vardet)

    def test_setname_should_Fail_when_length_less_than_two(self):
        target = Person("19720803-0000")
        result = target.setName("S")
        self.assertFalse(result)

    def test_setname_should_Fail_when_length_greater_than_fifty(self):
        target = Person("19720803-0000")
        result = target.setName("S"*55)
        self.assertFalse(result)


class PersonRegisterTest(unittest.TestCase):
    def test_when_adding_same_person_again_should_return_false(self):
        personReg = PersonRegister()
        res1  = personReg.add(Person("19720803-0000"))
        res2 = personReg.add(Person("19720803-0000"))
        self.assertFalse(res2)

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