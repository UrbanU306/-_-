from fake_math import divide as f_d
from true_math import divide as t_d

result1 = f_d(69, 3)
result2 = f_d(3, 0)
result3 = t_d(49, 7)
result4 = t_d(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)


# result1 = fake_divide(69, 3)
# result2 = fake_divide(3, 0)
# result3 = true_divide(49, 7)
# result4 = true_divide(15, 0)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
#
# Вывод на консоль:
# 23.0
# Ошибка
# 7.0
# inf