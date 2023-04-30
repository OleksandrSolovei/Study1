"""домашнє завдання 10"""
from math import pow as pw, sqrt as sq

def broken_calc():
    """помилка калькулятора"""
    print('Калькулятор працює некоректно. Дії під таким номером не існує!')


def mnosghennia(number1, number2):
    """добуток двох чисел"""
    return number1 * number2


def stupin_of_num(number, stupin_of_number):
    """піднесення до ступеня"""
    return pw(number, stupin_of_number)


def koren_kvadr(number):
    """обчислення квадратного кореня числа"""
    return sq(number)


def koren_kubich(number):
    """обчислює корінь кубічний числа"""
    return number ** (1/3)


def menu():
    return print('Меню калькулятора:'
          '\n\t1. Множення'
          '\n\t2. Піднесення до ступеня'
          '\n\t3. Квадратний корінь'
          '\n\t4. Кубічний корінь'
          '\n\t5. Вихід')


def input_number_1():
    """запит у користувача числа для розрахунків"""
    input_number = input('Введіть число: ')
    return int(input_number)



def input_number_2():
    """запит у користувача другого числа"""
    input_number = input('Введіть друге число: ')
    return int(input_number)

STOP_WORK = False
while not STOP_WORK:
    menu()
    vubir = input("Оберіть дію за номером в меню: ")
    if vubir.isdigit():
        match int(vubir):
            case 1:
                number1 = input_number_1()
                if number1:
                    number2 = input_number_2()
                    if number2:
                        total = mnosghennia(number1, number2)
                        print(f'{number1} * {number2} = {total}')
                    else:
                        broken_calc()
                else:
                    broken_calc()

            case 2:
                number1 = input_number_1()
                if number1:
                    stup = input_number_2()
                    if stup:
                        total = stupin_of_num(number1, stup)
                        print(f'{number1} в ступені {stup} = {total}')
                    else:
                        broken_calc()
                else:
                    broken_calc()

            case 3:
                number1 = input_number_1()
                kor = koren_kvadr(number1)
                print(f'Корень квадратний числа {number1} = {kor}')
            case 4:
                number1 = input_number_1()
                kor = koren_kubich(number1)
                print(f'Корень кубічний числа {number1} = {kor}')
            case 5:
                print('Роботу калькулятора завершено')
                STOP_WORK = True
    else:
        broken_calc()







