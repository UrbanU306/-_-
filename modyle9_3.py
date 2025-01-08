# Задача:
# Дано 2 списка:
# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']

# Необходимо создать 2 генераторных сборки:

# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых
# позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

# Пример результата выполнения программы:
# Пример выполнения кода:
# print(list(first_result))
# print(list(second_result))
# Вывод в консоль:
# [1, 2]
# [False, False, True]



first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# высчитывает разницу длин строк из списков first и second, если их длины не равны
first_result = (len(first) - len(second) for (first, second) in zip(first, second) if len(first) != len(second))

# результаты сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
