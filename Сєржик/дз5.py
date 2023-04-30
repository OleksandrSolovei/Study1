from statistics import mean
from collections import namedtuple
#
# # Завдання 1
# pib = input('Введіть ваше ПІБ: ')
# ran = pib.split()
# if len(ran) == 3:
#     for i in ran:
#         if not i.isalpha() or not i.istitle():
#             print('Ви ввели не коректний ПІБ')
#             break
#         else:
#             print(i)
# else:
#     print('Ви ввели не коректний ПІБ')
#
# print()
#
# Завдання 2
# num = input('Введіть розмір діапазону: ')
# if not num.isdigit() or int(num) < 5:
#     print('Ви ввели не коректний розмір діапазону')
# else:
#     num = int(num)
#     my_tuple = tuple(range(num))
#     print(my_tuple)
#     print(f'sum = {my_tuple[1] + my_tuple[-2] + mean(my_tuple)}')
#
# print()
#
# # Завдання 3
# r = input("input r: ")
# g = input("input g: ")
# b = input("input b: ")
# while not r.isdigit() or not 0 < int(r) <= 255 \
#         or not g.isdigit() or not 0 < int(g) <= 255 \
#         or not b.isdigit() or not 0 < int(b) <= 255:
#     r = input("input r: ")
#     g = input("input g: ")
#     b = input("input b: ")
# else:
#     r = int(r)
#     g = int(g)
#     b = int(b)
#     Colors = namedtuple('Colors', 'r g b')
#     colors = Colors(r, g, b)
#     print(colors)
#
# print()

# # Завдання 4
# Marks = namedtuple('Оцiнки', 'алгебра геометрія історія інформатика географія')
# marks1 = Marks(5, 5, 5, 5, 5)
# print(marks1)
# marks2 = Marks(4, 5, 4, 4, 3)
# print(marks2)
#
# print()

# Завдання 5
my_tuple = tuple(input("Введiть послідовність чисел через пробiл: ").split())
print(sorted(my_tuple))

# Завдання  6 - не встиг виконати, вибачте