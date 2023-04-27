# https://realpython.com/python-getter-setter/#using-properties-instead-of-getters-and-setters-the-python-way

from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

Tosin = Employee('Tosin', '2001-02-07')
print(Tosin.name)
print(Tosin.birth_date)

Tosin.name = "John Orenaike"
print(Tosin.name)
