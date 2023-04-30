# не працює останній case
my_list = [3, 4, 5]
my_list_new = []
for num in my_list:
    res = num % 2
    if num != 0:
        my_list_new.append(num)
print(my_list_new)
print('Меню:\n\t1. Додати всі числа\n\t2. Перемножити всі числа')
komanda = int(input('Оберіть дію:'))
total = 0
match komanda:
    case 1:
        for i in my_list_new:
            total += i
    case 2:
        for i in range(len(my_list_new)):
            total *= my_list_new[i]

print(my_list_new)
print(total)
