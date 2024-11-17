# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код
#   остался рабочим и выглядел следующим образом:
#data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])]
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.
# Помогите сокурснику осуществить его задумку.
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
# Входные данные (применение функции):
#data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
# result = calculate_structure_sum(data_structure)
# print(result)
# Выходные данные (консоль):   99

def calculate_sum_and_length(*args):
    sum = 0
    for element in args:
        if isinstance(element, str):
            sum += len(element)
        elif isinstance(element, int):
            sum += element
        elif isinstance(element, float):
            sum += element
        elif isinstance(element, bool):
            sum += element
        elif isinstance(element, list):
            sum += calculate_sum_and_length(*element)
        elif isinstance(element, tuple):
            sum += calculate_sum_and_length(*element)
        elif isinstance(element, set):
            sum += calculate_sum_and_length(*element)
        elif isinstance(element, dict):
            sum += calculate_sum_and_length(*tuple(element.items()))
    return sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_sum_and_length(data_structure)
print(result)
