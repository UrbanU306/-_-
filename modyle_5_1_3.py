# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты
# сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями
# лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
# Пример результата выполнения программы:
#
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# print(h1)
# print(h2)
# print(h1 == h2) # __eq__
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
# h1 += 10 # __iadd__
# print(h1)
# h2 = 10 + h2 # __radd__
# print(h2)
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False


class House:
    def __init__(self, name, number_of_floors):  # Создаем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:  # Вывод на экран(в консоль) числа от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # Дополним методами из задачи:
    # Оператор равенства, ==
    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    # Оператор сложения, +
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Сложение с присваиванием +=
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Отражённое сложение
    def __radd__(self, value):
        return self.__add__(value)

    # Определяет поведение оператора больше >
    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    # Определяет поведение оператора больше или равно >=
    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    # Определяет поведение оператора меньше <
    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    # Определяет поведение оператора меньше или равно <=
    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    # Определяет поведение оператора неравно !=
    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)
print(" __eq__ начальное")
print(h1 == h2)  # __eq__
print(" __add__ +10")
h1 = h1 + 10  # __add__
print(h1)
print(" __eq__ повторное")
print(h1 == h2)
print("__iadd__ += 10")
h1 += 10  # __iadd__
print(h1)
print("__radd__ Отражённое сложение 10+")
h2 = 10 + h2  # __radd__
print(h2)
print("__gt__")
print(h1 > h2)  # __gt__
print("__ge__")
print(h1 >= h2)  # __ge__
print("__lt__")
print(h1 < h2)  # __lt__
print("__le__")
print(h1 <= h2)  # __le__
print("__ne__")
print(h1 != h2)  # __ne__

#
# print("__len__")
# print(len(h1))
# print(len(h2))
#
# print("__str__")
# print(h1)
# print(h2)
