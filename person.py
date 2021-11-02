class Person:
    def __init__(self,personNumber:str):
        self._name=""
        self._personalNumber = personNumber

    def setName(self,name:str)->bool:
        if len(name) < 2:
             return False
        if len(name) > 50:
             return False
        self._name = name
        return True

    def getName(self):
        return self._name

    def getPersonalNumber(self):
        return self._personalNumber


class PersonRegister:
    def __init__(self):
        self._persons = {}

    def getPerson(self, personNummer):
        if not personNummer in self._persons:
            return None
        return self._persons[personNummer]

    def add(self,person:Person):
        if person.getPersonalNumber() in self._persons:
            return False
        self._persons[person.getPersonalNumber()] = person
        return True

# personReg = PersonRegister()
# res1  = personReg.add(Person("19720803-0000"))
# res2 = personReg.add(Person("19720803-2800"))
# print(res1)
# print(res2)