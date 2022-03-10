class Customer ():
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_info(self):
        return f'Клиент "{self.name} {self.surname}". Баланс:{self.balance} руб.'

c_1= Customer('Иван','Петров','50')
print(c_1.get_info())