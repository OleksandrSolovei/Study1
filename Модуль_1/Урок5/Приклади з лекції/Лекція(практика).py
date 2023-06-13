from collections import namedtuple
while True:
    r = input("Введіть значення від 0 до 255 включно: ")
    g = input("Введіть значення від 0 до 255 включно: ")
    b = input("Введіть значення від 0 до 255 включно: ")
    if r.isdigit() and g.isdigit() and b.isdigit():
        r = int(r)
        g = int(g)
        b = int(b)
        my_taple = namedtuple('RGB', 'red green blue')
        user_value = my_taple(r, g, b)
        print(user_value)
        break
    else:
        print('Сталась помилка...')




