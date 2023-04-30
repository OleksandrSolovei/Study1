import math

def my_sum(a, b):
    total = a + b
    return total


def my_vidnim(a, b):
    total = a - b
    return total

def my_mnosgh(a, b):
    total = a * b
    return total

def my_dil(a, b):
    total = a / b
    return total

def my_kvad_kor(a):
    total = a**2
    return total

def my_kub_kor(a):
    total = a
    return total

print('\nМеню:',
      '1. Додавання',
      '2. Віднімання',
      '3. Множення',
      '4. Ділення',
      '5. Піднесення до квадратного кореня',
      '6. Піднесення до кубічного кореня',
      '7. Вихід', sep="\n\t")
ectoin = int(input('Вкажіть дію: '))
match ectoin:
    case 1:
        first_number = int(input('Введіть число: '))
        second_number = int(input('Введіть друге число: '))
        result = my_sum(first_number, second_number)
        print('Відповідь = ', result)
    case 2:
        first_number = int(input('Введіть число: '))
        second_number = int(input('Введіть друге число: '))
        result = my_vidnim(first_number, second_number)
        print('Відповідь = ', result)
    case 3:
        first_number = int(input('Введіть число: '))
        second_number = int(input('Введіть друге число: '))
        result = my_mnosgh(first_number, second_number)
        print('Відповідь = ', result)
    case 4:
        first_number = int(input('Введіть число: '))
        second_number = int(input('Введіть друге число: '))
        while second_number == 0:
            second_number = int(input('Неможливо поділити на нуль. Введіть друге число, що не дорівнює нулю: '))
        else:
            result = my_dil(first_number, second_number)
            print('Відповідь = ', result)
    case 5:
        first_number = int(input('Введіть число: '))
        result = my_kvad_kor(first_number)
        print('Відповідь = ', result)
    case 6:
        first_number = int(input('Введіть число: '))
        result = my_kub_kor(first_number)
        print('Відповідь = ', result)
    case 7:
        print('Вихід')

    # first_number = input('Введіть число: ')
    # second_number = input('Введіть друге число: ')