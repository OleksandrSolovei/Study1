# """виконання домашнього завдання до уроку 10"""
# from math import pow as pw, sqrt as sq
#
# # Завдання 3
#
# def print_error_broken_calc():
#     """функцiя виводить на друк помилку калькулятора"""
#     print("Калькулятор поламався :-)")
#
#
# def print_error_num():
#     """функцiя виводить на друк помилку введення числе вiд користувача"""
#     print("Ведено не корректнi числа")
#
#
# def result_stupin(number, power):
#     """функцiя пiдносить число до ступеня"""
#     return pw(number, power)
#
#
# def result_kv_korin(number):
#     """функція обчислює квадратний корінь числа"""
#     return sq(number)
#
#
# def result_kub_korin(number):
#     """функція обчислює кубічний корінь числа"""
#     return number ** (1/3)
#
#
# def result_input_number(my_param=''):
#     """функція зчитує введене число користувачем"""
#     return input(f"Введiть {my_param} число: ")
#
#
# def print_menu_calc():
#     """функція виводить меню калькулятора"""
#     return print('Меню програми Калькулятор:'
#                  '\n\t1.зведення в ступінь',
#                  '2.квадратний корінь',
#                  '3.кубічний корінь',
#                  '0.вихiд', sep='\n\t')
#
# STOP_CALC = False
# while not STOP_CALC:
#     print_menu_calc()
#     result = input('Ваш вибiр: ')
#     if result.isdigit():
#         match int(result):
#             case 1:
#                 num1 = result_input_number()
#                 stupin = input("Введiть ступiнь: ")
#                 if num1.isdigit() and stupin.isdigit():
#                     print(f'Результат зведення {num1} в ступінь {stupin} '
#                           f'= {result_stupin(int(num1), int(stupin))}')
#                 else:
#                     print_error_num()
#             case 2:
#                 num1 = result_input_number()
#                 if num1.isdigit():
#                     print(f'Квадратний корінь з числа {num1} = {result_kv_korin(int(num1))}')
#                 else:
#                     print_error_num()
#             case 3:
#                 num1 = result_input_number()
#                 if num1.isdigit():
#                     print(f'Кубічний корінь з числа {num1} = {result_kub_korin(int(num1))}')
#                 else:
#                     print_error_num()
#             case 0:
#                 print('Роботу калькулятора завершено')
#                 STOP_CALC = True
#
#     else:
#         print_error_broken_calc()


#
# Завдання 4


def add_tuple(mgz):
    """це функція, яка запитує дані у користувача та зібрані дані
    у вигляді кортежу додає до створеного списку на початок списку"""

    new_text = input('Input some text: ').split(",")
    new_tuple = tuple(x for x in new_text)
    mgz.insert(0, new_tuple)


magazine = []
for i in range(5):
    add_tuple(magazine)

print(magazine)
