from statistics import mean
ran = input('Введіть діапазон: ')
if not ran.isdigit() or int(ran) < 5:
    print('Некоректно введені дані!')
else:
    ran = int(ran)
    my_tuple = tuple(range(ran))
    print(my_tuple)
    print(f'Сума = {my_tuple[1] + my_tuple[-2] + mean(my_tuple)}')
