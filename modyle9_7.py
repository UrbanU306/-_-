# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)

# Результат консоли:
# Простое
# 11

# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three


def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if all((x % i) != 0 for i in range(2, int(x ** 0.5) + 1)): # проверка числа на простое и составное и вывод
            print('Простое')
        else:
            print('Составное')
        return x

    return wrapper


@is_prime
def sum_three(*args):  # sum_three суммирует любое количество числовых аргументов
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)
