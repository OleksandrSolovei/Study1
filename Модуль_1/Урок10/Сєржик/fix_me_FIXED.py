"""
Відкрийте файл fix_me.py із папки homework. Використовуючи звичайний текстовий редактор (Notepad),
виправте всі помилки оформлення коду згідно з PEP 8.
"""

from math import pi, e, pow as pw


RND_SUM = 5
count = int(input('Введите количество повторов: '))
print(RND_SUM * count)
print(pi * RND_SUM * count)
print(e * 2)

while RND_SUM >= 0 :
    RND_SUM -= 1

MY_STR = 'my string'
NEW_SUM = 0
for elem in MY_STR:
    NEW_SUM += pw(MY_STR.find(elem), 2)
    print("sum =", NEW_SUM)


def my_function(atr=1):
    """description of my_function"""
    print('atr', atr)


print(my_function(5))
