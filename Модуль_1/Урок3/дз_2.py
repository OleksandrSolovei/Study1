import math
x = int(input('Введіть значення "x": '))
if math.pi * -1 <= x <= math.pi:
    y = math.cos(3 * x)
    print(f'Відповідь: y = {y}')
else:
    print('"x" не відповідає параметрам.')