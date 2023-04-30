int_list = [2, 15, 4, 7, 9, 36, 17]
new_list = []
for i in int_list:
    if not i % 2 == 0:
        new_list.append(i)
print(new_list)
repead = int(input('Введіть кількість повторів для списку: '))
ran = range(repead)
for i in ran:
    print(new_list)
clean_int_list = int_list.clear()
print(f'Список int_list очищено та має вигляд: {int_list}')
