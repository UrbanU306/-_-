# Ваша задача:
# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function,
#     Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# Файл с кодом module_4_2.py загрузите на GitHub репозиторий и пришлите ссылку на него.


def test_function():  # Создайте новую функцию test_function
    def inner_function():  # Создайте внутри test_function другую функцию - inner_function
        print("Я в области видимости функции test_function")  # печать значение "Я в области видимости функции test_function"

    inner_function()  # Здесь ничего не возвращает


inner_function()  # При вызове в области test_function приводит к ошибке.
