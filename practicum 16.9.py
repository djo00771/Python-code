# Класс прямоугольник --------------------------------------------------------------------------------------------------
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        if self.width != self.height:
            return self.width * self.height
        else:
            print('Это не  Прямоугольник. Посетите https://clck.ru/f4jUr')
            exit()


print('Расчет площади прямоугольника по двум параметрам')
obj = Rectangle (int(input('Введите ширину = ')), int(input('Введите высоту = ')))
print(f'Ширина {obj.get_width()} \nВысота {obj.get_height()} \nПлощадь объекта = {obj.get_area()}')


# Класс пользователь ---------------------------------------------------------------------------------------------------
class User():
    def __init__(self, fist_name, name, city, balance):
        self.first_name = fist_name
        self.name = name
        self.city = city
        self.balance = balance

    def get_first_name(self):
        return self.first_name

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_balance(self):
        return self.balance

    def get_users(self):

        return f'Новый пользователь - {self.first_name} {self.name} \nГород герой - {self.city} \nБаланс = {self.balance}'


first_name = input('Введите фамилию: ')
name = input('Введите имя: ')
city = input('Ваш город: ')
balance = int(input('Ваш баланс: '))

print('Регистрация пользователя')
user1 = User (first_name, name, city, balance)
print(user1.get_users().title())


# Класс Кошкин корпоратив ----------------------------------------------------------------------------------------------

class PetCorporate(User):
    def __str__(self):
        return f'''"{self.first_name} {self.name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.first_name} {self.name},г. {self.city}'


pers_1 = PetCorporate('Иван', 'Петров', 'Москва', 50)
pers_2 = PetCorporate('Владимир', 'Зайцев', 'Кострома', 50)
pers_3 = PetCorporate('Олеся', 'Янина', 'Новосибирск', 50)

guest_list = [pers_1, pers_2, pers_3]

for guest in guest_list:
    print(guest.get_guest())
