#
from collections import namedtuple
uchen = input('Введіть прізвище учня: ')
print('Вкажіть кількість балів:')
a = int(input('Алгебра: '))
b = int(input('Геометрія: '))
c = int(input('Історія: '))
d = int(input('Інформатика: '))
e = int(input('Географія: '))
tabel = namedtuple(uchen, 'алгебра геометрія історія інформатика географія')
Tabel = tabel(a, b, c, d, e)
print(Tabel)
