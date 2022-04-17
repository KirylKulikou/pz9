# задание 3

class Wolker:

    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Wolker):

    def get_full_name(self):
        return f'И.Ф. сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        self._income = sum(self._income.values())
        return f'Доход составляет: {self._income} рублей'


position = Position("Иван", "Иванов", "тракторист", зп = 50000, премия = 5000)
print(position.get_full_name())
print(position.get_total_income())