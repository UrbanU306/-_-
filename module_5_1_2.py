# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


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


h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)
# h1.go_to(5)
# h2.go_to(10)


print("__len__")
print(len(h1))
print(len(h2))

print("__str__")
print(h1)
print(h2)