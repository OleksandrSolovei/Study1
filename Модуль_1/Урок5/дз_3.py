# висвести на екран кортеж з параметрами кольорів в діапазоні від 0 до 255
from collections import namedtuple
print('Введіть параметр кольору в діапазоні від 0 до 255:')
znachennia = int(input('Введіть параметр green: '))
if 0 <= znachennia <= 255:
    green = znachennia
znachennia = int(input('Введіть параметр blue: '))
if 0 <= znachennia <= 255:
    blue = znachennia
znachennia = int(input('Введіть параметр red: '))
if 0 <= znachennia <= 255:
    red = znachennia
paramertu = namedtuple('Colors', 'green, blue, red')
colors = paramertu(green, blue, red)
print(colors)
