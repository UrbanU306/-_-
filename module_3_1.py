calls = 0


# Функция для подсчета вызовов
def count_calls():
    global calls  # Указываем, что мы используем глобальную переменную
    calls += 1  # Увеличиваем счетчик вызовов на 1


# Функция для обработки строки
def string_info(string):
    count_calls()
    length = len(string)  # Длина строки
    upper_case = string.upper()  # Строка в верхнем регистре
    lower_case = string.lower()  # Строка в нижнем регистре
    return (length, upper_case, lower_case)  # Возвращаем кортеж


# Функция для проверки вхождения строки в список
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()  # Приводим строку и элементы списка к н.регистру для сравнения
    for item in list_to_search:
        if string == item.lower():
            return True
    return False  # Возвращаем результат проверки


# Вызов функций с произвольными данными
result1 = string_info("Привет Я РОДИЛСЯ")

result2 = is_contains("привет я РОДИЛСЯ", ['привет я родился'])

print("Результат из string_info:", result1)
print()
print("Результат из is_contains:", result2)
print()
print("Количество вызовов функций:", calls)
