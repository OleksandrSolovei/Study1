import math
#
# # Завдання 1
# a = int(input("Введiть значення числа а: "))
# b = int(input("Введiть значення числа b: "))
# while b < a:
#     print("Число b повинно бути бiльше за число a")
#     a = int(input("Введiть значення елементу а: "))
#     b = int(input("Введiть значення елементу b: "))
# else:
#     total = 0
#     for i in range(a, b + 1):
#         total += i
#     print("total = ", total)
#
# print()
#
# # Завдання 2
# num = int(input("Введіть число для обчислення його факторіалу: "))
# print(f'Факторiалом числа {num} є значення {math.factorial(num)}')
#
# print()
#
# # Завдання 3
# n = 10
# for i in range(n):
#     print('* ' * (i + 1))
#
# print()
#
# # Завдання 4
# a = int(input("Введiть значення числа а: "))
# b = int(input("Введiть значення числа b: "))
# while b < a:
#     print("Число b повинно бути бiльше за число a")
#     a = int(input("Введiть значення елементу а: "))
#     b = int(input("Введiть значення елементу b: "))
# else:
#     my_range = range(a, b + 1)
#     print(list(my_range))
#     print(f'range sum = {sum(my_range)}')
#     avg = sum(my_range) / len(my_range)
#     print(f'average = {avg}')
#     total = 0
#     for i in my_range:
#         if i % avg == 0:
#             total += i
#     print("total = ", total)
#
# print()

# Завдання 5
h = input("Введiть висоту (h) прямокутника: ")
w = input("Введiть ширину (w) прямокутника: ")
if h.isdigit() and w.isdigit():
    h = int(h)
    w = int(w)
    for i in range(h):
        for j in range(w):
            if i == h-1 or i == 0:
                print('*', end='')
            elif i != 0 and (j == 0 or j == w-1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
else:
    print("Введено не корретнi данi")

print()

# # Завдання 6
# login = 'my_login'
# password = '12345'
# x = 0
# while x < 3:
#     x += 1
#     print(x)
#     input_login = input('Please, input your login: ')
#     input_pass = input('Please, input your password: ')
#     if input_login == login and input_pass == password:
#         print(f'Авторизацію успішно пройдено з {x} спроби')
#         break
#
# print()
#
# # теж саме, але за допомогою циклу for
# for i in range(3):
#     print(i+1)
#     input_login = input('Please, input your login: ')
#     input_pass = input('Please, input your password: ')
#     if input_login == login and input_pass == password:
#         print(f'Авторизацію успішно пройдено з {i+1} спроби')
#         break
