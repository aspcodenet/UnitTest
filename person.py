class Person:
    def __init__(self,name:str,personNumber:str):
        self._name=name
        self._personalNumber = personNumber

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
