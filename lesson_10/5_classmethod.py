import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)

    @property
    def age(self):
        return self._age


if __name__ == "__main__":
    person = Person.from_birth_year("Sasha", 1997)
    print(person.name, person.age)
