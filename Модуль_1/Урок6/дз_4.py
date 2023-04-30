kil_sumv = int(input('Зазначте кількість елементів, що мають входити до списку: '))
ran = range(kil_sumv)
my_list = []
for i in ran:
    znach = input('Введіть значення елементу:')
    my_list.append(znach)
print(f'Ваш список елементів: {my_list}')
print('Меню:\n\t1. Вивести список у зворотньому порядку\n\t2. Вивести список за зростанням')
diia = int(input('Оберіть дію: '))
match diia:
    case 1:
        print(my_list[::-1])
    case 2:
        my_list.sort()
        print(my_list)

