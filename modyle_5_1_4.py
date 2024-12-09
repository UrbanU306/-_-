# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
# # Удаление объектов
# del h2
# del h3
# print(House.houses_history)
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        object = super().__new__(cls)
        cls.houses_history.append(args[0])
        return object

    def __init__(self, name, number_of_floors):  # Создаем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    # def go_to(self, new_floor):
    #     if 0 < new_floor <= self.number_of_floors:  # Вывод на экран(в консоль) числа от 1 до new_floor
    #         for floor in range(1, new_floor + 1):
    #             print(floor)
    #     else:
    #         print("Такого этажа не существует")
    #
    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    #
    # # Дополним методами из задачи:
    # # Оператор равенства, ==
    # def __eq__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors == other.number_of_floors
    #
    # # Оператор сложения, +
    # def __add__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floors += value
    #     return self
    #
    # # Сложение с присваиванием +=
    # def __iadd__(self, value):
    #     if isinstance(value, int):
    #         self.number_of_floors += value
    #     return self
    #
    # # Отражённое сложение
    # def __radd__(self, value):
    #     return self.__add__(value)
    #
    # # Определяет поведение оператора больше >
    # def __gt__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors > other.number_of_floors
    #
    # # Определяет поведение оператора больше или равно >=
    # def __ge__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors >= other.number_of_floors
    #
    # # Определяет поведение оператора меньше <
    # def __lt__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors < other.number_of_floors
    #
    # # Определяет поведение оператора меньше или равно <=
    # def __le__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors <= other.number_of_floors
    #
    # # Определяет поведение оператора неравно !=
    # def __ne__(self, other):
    #     if isinstance(other.number_of_floors, int) and isinstance(other, House):
    #         return self.number_of_floors != other.number_of_floors


h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)
h2 = House("ЖК Акация", 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)