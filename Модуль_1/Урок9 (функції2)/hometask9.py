"""hometask9"""

import math

# Завдання 2
def is_palindrome(new_str):
    """is_palindrome"""
    if len(new_str) <= 1:
        return True
    else:
        if new_str[0] == new_str[-1]:
            return is_palindrome(new_str[1:-1])
        else:
            return False

my_string = input('Введіть будь-яке слово: ')
if is_palindrome(my_string):
    print('Це паліндром')
else:
    print("Рядок не є паліндромом ")

print()

# Завдання 3
def total_ways(n_st):
    """total_ways"""
    if n_st < 0:
        return 0
    if n_st == 0:
        return 1
    return total_ways(n_st - 1) + total_ways(n_st - 2)


def input_function():
    """input_function"""
    return input('Введіть номер сходинки: ')


n = input_function()
while not n.isdigit():
    n = input_function()
else:
    print('Кількість способів піднятися на сходинку:', total_ways(int(n)))

print()

# Завдання 4
def calculate_sum(a, b):
    """is_palindrome"""
    if a == b:
        return b
    else:
        return b + calculate_sum(a, b - 1)


value_a = int(input('Input value a: '))
value_b = int(input('Input value b: '))
if value_b > value_a:
    print(calculate_sum(value_a, value_b))

print()

# Завдання 5
def quadratic_equation(arg_a, arg_b, arg_c):
    """quadratic_equation"""
    x_1 = None
    x_2 = None
    def calc_rezult(arg_a, arg_b, arg_c):
        """calc_rezult"""
        disc = arg_b * arg_b - 4 * arg_a * arg_c
        if disc < 0:
            print('Рівняння не має рішення')
        else:
            root = math.sqrt(disc)
            x_1 = (-arg_b + root) / (2 * arg_a)
            if disc != 0:
                x_2 = (-arg_b - root) / (2 * arg_a)
                print(f'Корінь рівняння x1 = {x_1} i корінь рівняння x2 = {x_2}')
            else:
                print(f'Єдиним рішенням є корінь рівняння x1 = {x_1}')

    calc_rezult(arg_a, arg_b, arg_c)

a_1, b_1, c_1 = map(int, input('Введiть три цiлих числа через пробiл: ').split())
quadratic_equation(a_1, b_1, c_1)
