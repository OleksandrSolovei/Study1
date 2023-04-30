my_list1 = [22, 1, 2, 3, 4]
my_list2 = [55, 6, 7, 8, 9]
chuslo1 = int(input('Введіть ціле число до першого списку: '))
if not chuslo1 in my_list2:
    if chuslo1 in my_list1:
        print('Чило не може бути додане, тому що вже є в одному зі списків!')
    else:
        my_list1.append(chuslo1)
else:
    print(f'Число {chuslo1} не може бути додане до списку №1, тому що вже є в списку №2!')
chuslo2 = int(input('Введіть ціле число до другого списку: '))
if not chuslo2 in my_list1:
    if chuslo2 in my_list2:
        print('Чило не може бути додане, тому що вже є в одному зі списків!')
    else:
        my_list2.append(chuslo2)
else:
    print(f'Число {chuslo2} не може бути додане до списку №2, тому що вже є в списку №1!')
print(my_list1[::-1])
print(my_list2[::-1])
print(sorted(my_list1))
print(sorted(my_list2))
print(sorted(my_list1, reverse=True))
print(sorted(my_list2, reverse=True))
