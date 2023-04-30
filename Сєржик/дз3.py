import math

def print_error_num():
      print("Ведено не корректнi числа")
def print_error_broken_calc():
       print("Калькулятор поламався :-)")


# Завдання 1
name = input("Будь ласка, введіть своє ім\'я: ")
my_name = "Сергій"
print("Вітаю, тезка:-)" if name == my_name else "Привіт " + name)

print()

# Завдання 2
x = input("Для обчислення функції 𝑦 = cos(3x) введiть значення x: ")
if x.isdigit():
    x = float(x)
    if -math.pi <= x <= math.pi:
      y = math.cos(3 * x)
      # Знайшов в інтернетi формулу переведення градусів у радіани: градуси * Пi/180
      rad = y * math.pi / 180
      print(f"Результат y = {y}, виражений у радiанах")
    else:
          print("Введене число x не відповідає умові задачі")
else:
    print("Ви ввели не корректне значення x")

print()

# Завдання 3 - не виконано. я не розумію що тут потрібно зробити, аналогічно минулому завданню в попередньому ДЗ


# Завдання 4
print("Меню програми Калькулятор:")
print('\t1.додавання',
      '2.віднімання',
      '3.множення',
      '4.ділення',
      '5.зведення в ступінь',
      '6.квадратний корінь',
      '7.кубічний корінь',
      '8.синус числа',
      '9.косинус числа',
      '10.тангенс числа', sep='\n\t')
result = input("Виберiть одну з операцій: ")
if result.isdigit():
      result = int(result)
      match result:
            case 1:
                  a = input("Введiть перше число: ")
                  b = input("Введiть друге число: ")
                  if a.isdigit() and b.isdigit():
                        a = int(a)
                        b = int(b)
                        print(f'Результат додавання {a} + {b} = {a + b}')
                  else:
                        print_error_num()
            case 2:
                  a = input("Введiть перше число: ")
                  b = input("Введiть друге число: ")
                  if a.isdigit() and b.isdigit():
                        a = int(a)
                        b = int(b)
                        print(f'Результат віднімання {a} - {b} = {a - b}')
                  else:
                        print_error_num()
            case 3:
                  a = input("Введiть перше число: ")
                  b = input("Введiть друге число: ")
                  if a.isdigit() and b.isdigit():
                        a = int(a)
                        b = int(b)
                        print(f'Результат множення {a} * {b} = {a * b}')
                  else:
                         print_error_num()
            case 4:
                  a = input("Введiть перше число: ")
                  b = input("Введiть друге число: ")
                  if a.isdigit() and b.isdigit():
                        a = int(a)
                        b = int(b)
                        try:
                              print(f'Результат ділення {a} / {b} = {a / b}')
                        except ZeroDivisionError:
                              print('Помилка. На нуль ділити не можна')
                  else:
                        print_error_num()
            case 5:
                  num = input("Введiть число: ")
                  x = input("Введiть ступiнь: ")
                  if a.isdigit() and x.isdigit():
                        a = int(num)
                        x = int(x)
                        print(f'Результат зведення {num} в ступінь {x} = {pow(num, x)}')
                  else:
                         print_error_num()
            case 6:
                  num = input("Введiть число: ")
                  if num.isdigit():
                        num = int(num)
                        print(f'Квадратний корінь з числа {num} = {math.sqrt(num)}')
                  else:
                         print_error_num()
            case 7:
                  num = input("Введiть число: ")
                  if num.isdigit():
                        num = int(num)
                        print(f'Кубічний корінь з числа {num} = {num ** (1/3)}')
                  else:
                        print_error_num()
            case 8:
                  num = input("Введiть число: ")
                  if num.isdigit():
                        num = int(num)
                        print(f'Cинус числа {num} = {math.sin(num)}')
                  else:
                        print_error_num()
            case 9:
                  num = input("Введiть число: ")
                  if num.isdigit():
                        num = int(num)
                        print(f'Косинус числа {num} = {math.cos(num)}')
                  else:
                        print_error_num()
            case 10:
                  num = input("Введiть число: ")
                  if num.isdigit():
                        num = int(num)
                        print(f'Тангенс числа {num} = {math.tan(num)}')
                  else:
                        print_error_num()
            case _:
                  print_error_broken_calc()
else:
      print_error_broken_calc()

print()

# Завдання 5
num = input("Введiть число для перевірки на ознаку парності: ")
if num.isdigit():
      num = int(num)
      print("Число парне" if num % 2 == 0 else "Число не парне")
else:
      print_error_num()

print()

# Завдання 6 - вирішив зробити перевірку за номером дня (від 1 до 7)
num_day = input("Введiть номер дня тижня вiд 1 до 7: ")
if num_day.isdigit():
      num_day = int(num_day)
      if 1 <= num_day <= 5:
            print("Сьогодні на роботу")
      elif 6 <= num_day <= 7:
            print("Сьогодні вихідний")
      else:
            print("Такого дня не існує")
else:
      print_error_num()





