import math
# Завдання 1
word_1 = input("Введите первое слово: ")
word_2 = input("Введите второе слово: ")
print(word_1, word_2, sep=",")

# Завдання 2
number_1 = int(input("Введите первое целое число: "))
number_2 = int(input("Введите второе целое число: "))
number_3 = int(input("Введите третье целое число: "))
print('{} * {} * {} = {}'.format(number_1, number_2, number_3, number_1 * number_2 * number_3))
# або ось так
print(f"{number_1} * {number_2} * {number_3} = {number_1 * number_2 * number_3}")

# Завдання 3 - я не понял что тут нужно сделать, поэтому не выполнил задание

# Завдання 4
text = input("Введите фразу длиной 10 символов: ")
if len(text) != 10:
    print("Error")
else:
    sum_of_char = 0
    for i in text:
        sum_of_char = sum_of_char + ord(i)
        print(sum_of_char)

## Завдання 5
text = input("Input text: ")
rev_text = ""
for i in text:
    rev_text = i + rev_text
print("Reversed text: ", rev_text)

## Завдання 6
rad = int(input("Введите радиус круга: "))
print("Площадь круга = ", math.pi * math.pow(rad, 2))

# Завдання 7
length = 700
velocity = 90
driving_time = length / velocity
hours = math.floor(driving_time)
minutes = round((driving_time - hours) * 60)
print('Время поездки {} часов {} минут'.format(hours, minutes))

# Завдання 8
name = input("Input your name: ")
age = int(input("Input you age: "))
print("My name is " + name + " and I am " + str(age))








