class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class InvitedPersons(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def __str__(self):
        return f'{self.name}, г.{self.city}, статус "{self.status}"'


v_1 = InvitedPersons('Иван Петров', 'Москва', 'Наставник')
v_2 = InvitedPersons('Петр Иванов', 'Балаково', 'Стажёр')
v_3 = InvitedPersons('Сидр Сидоров', 'Нижний Новгород', 'Волонтёр')

print(v_1)
print(v_2)
print(v_3)