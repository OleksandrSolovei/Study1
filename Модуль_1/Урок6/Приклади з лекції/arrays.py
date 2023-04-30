from array import *

# Оголошення масиву
# arrayIdentifierName = array(typecode, [Initializers])
my_array = array('i', [1, 2, 3, 4, 2])
print(my_array)
for i in my_array:
    print(i)
print(my_array.buffer_info())
print(sum(my_array))

print()

my_array1 = array('i', range(5, 11))
print(my_array1)
for i in my_array1:
    print(i)
print(my_array1.buffer_info())
print(sum(my_array1))
print()
# Доступ до окремих елементів через індекси
print(my_array[1])
print(my_array[-2])
print(my_array[0])

# Додати будь-яке значення масиву за допомогою методу append()
my_array.append(6)
print(my_array)

# Вставити значення масив за допомогою методу insert()
my_array.insert(0, 10)
print(my_array)

# Розширення python масиву за допомогою методу extend()
my_extend_array = array('i', [7, 8, 9, 10])
my_array.extend(my_extend_array)
print(my_array)

# Додати елементи зі списку до масиву, використовуючи метод fromlist()
c = [11, 12, 13]
my_array.fromlist(c)
print(my_array)

# Видаліть будь-який елемент масиву, використовуючи метод remove()
my_array.remove(4)
print(my_array)

# Видалити останній елемент масиву методом pop()
my_array.pop()
print(my_array)

# Отримати будь-який елемент через його індекс за допомогою методу index()
print(my_array.index(3))
# ValueError: array.index(x): x not in array
# print(my_array.index(15))

# Зворотний масив Python, використовуючи метод reverse()
my_array.reverse()
print(my_array)

# Отримати інформацію про буфер масиву за допомогою buffer_info(). Цей метод надає вам початкову адресу.
# Буфер масиву в пам'яті та кількість елементів в масиві.
my_array.buffer_info()

# Перевірка кількості входжень елементу за допомогою count()
print(my_array.count(3))

# Перетворити масив на рядок, використовуючи метод tounicode() - перетворює юнікод масив на рядок
my_char_array = array('u', ['s', 't', 'a', 'r', 't'])
x = ', '.join(my_char_array)
print(x)
print(my_char_array.tounicode())

# Перетворити масив на список Python з тими самими елементами, використовуючи метод tolist()
# Коли вам потрібний Python list об'єктів, ви можете використовувати tolist() метод,
# щоб перетворити ваш масив на список.
print(type(my_array))
print(c)
print(my_array)
c = my_array.tolist()
print(type(c))
print(c)

"""
Модуль array визначає масиви в python. Масиви дуже схожі на списки, але з обмеженням на тип даних та розмір кожного 
елементу.
Розмір і тип елемента в масиві визначається при його створенні і може набувати таких значень:
    Код типу     |     Тип у C    |    Тип у Python    |    Мінімальний розмір у байтах
        'b'      |   signed char  |         int        |                   1
        'B'      |  unsigned char |         int        |                   1
        'h'      |  signed short  |         int        |                   2
        'H'      | unsigned short |         int        |                   2
        'i'      |   signed int   |         int        |                   2
        'I'      |  unsigned int  |         int        |                   2
        'l'      |   signed long  |         int        |                   4
        'L'      |  unsigned long |         int        |                   4
        'q'      |  signed long   |       long int     |                   8
        'Q'      | unsigned long  |       long int     |                   8
        'f'      |      float     |       float        |                   4
        'd'      |     double     |       float        |                   8
Клас array.array(TypeCode [, ініціалізатор]) - новий масив, елементи якого обмежені TypeCode, та ініціалізатор, 
який має бути списком, об'єктом, який підтримує інтерфейс буфера, або об'єкт, що ітерується.
array.typecodes - рядок, що містить усі можливі типи в масиві.
Масиви змінюються. Масиви підтримують усі спискові методи (індексація, зрізи, множення, ітерації) та інші методи.

================================== Методи масивів (array) у python ==================================
array.typecode - TypeCode символ, використаний під час створення масиву.
array.itemsize - розмір байтів одного елемента в масиві.
array.append(х) - додавання елемента до кінця масиву.
array.buffer_info() - кортеж (комірка пам'яті, довжина). Корисно для низькорівневих операцій.
array.byteswap() - змінити порядок проходження байтів у кожному елементі масиву. Корисно при читанні даних із файлу, 
написаного на машині з іншим порядком байтів.
array.count(х) - повертає кількість входжень х до масиву.
array.extend(iter) - додавання елементів з об'єкта масив.
array.frombytes(b) - робить масив array з масиву байт. Кількість байт має бути кратна розміру одного елемента масиву.
array.fromfile(F, N) - читає N елементів із файлу і додає їх у кінець масиву. Файл має бути відкритим на бінарні 
читання. Якщо є менше елементів N, генерується виняток EOFError , але елементи, які були доступні, додаються в масив.
array.fromlist(список) - додавання елементів зі списку.
array.index(х) – номер першого входження x масив.
array.insert(n, х) - увімкнути новий пункт зі значенням х у масиві перед номером n. Негативні значення розглядаються 
щодо кінця масиву.
array.pop(i) - видаляє перший елемент з масиву і повертає його. За замовчуванням видаляється останній елемент.
array.remove(х) - видалити перше входження х із масиву.
array.reverse() - зворотний порядок елементів у масиві.
array.tobytes() - перетворення до байтів.
array.tofile(f) - запис масиву у відкритий файл.
array.tolist() - перетворення масиву на список.
"""