import math
vubir = int(input('Меню:\n\t1. Додавання\n\t2. Віднімання\n\t3. Множення\n\t4. Ділення\n\t5. Зведення в ступінь 2\n\t6. Квадратний корінь\n\t7. Кубічний корінь\n\t8. Синус\n\t9. Косинус\n\t10. Тангенс\n\t11. Вихід\nОберіть операцію: '))
match vubir:
    case 1:
        a = int(input('Введіть число "a": '))
        b = int(input('Введіть число "b": '))
        result = a + b
        print(result)
    case 2:
        a = int(input('Введіть число "a": '))
        b = int(input('Введіть число "b": '))
        result = a - b
        print(result)
    case 3:
        a = int(input('Введіть число "a": '))
        b = int(input('Введіть число "b": '))
        result = a * b
        print(result)
    case 4:
        a = int(input('Введіть число "a": '))
        b = int(input('Введіть число "b": '))
        result = a / b
        print(result)
    case 5:
        a = int(input('Введіть число: '))
        result = a ** 2
        print(result)
    case 6:
        a = int(input('Введіть число: '))
        result = math.sqrt(a)
        print(result)
    case 7:
        a = int(input('Введіть число: '))
        result = a ** (1. / 3.)
        print(result)
    case 8:
        a = int(input('Введіть число: '))
        result = math.sin(a)
        print(result)
    case 9:
        a = int(input('Введіть число: '))
        result = math.cos(a)
        print(result)
    case 10:
        a = int(input('Введіть число: '))
        result = math.tan(a)
        print(result)
    case 11:
        print('Вихід')
    case _:
        print('Error')