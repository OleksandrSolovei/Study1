# якась дурниця вийшла
my_dict = dict()
poch_pos = input('Введіть початкове посилання: ')
kor_nazv = input('Введіть скорочену назву посилання: ')
my_dict[poch_pos] = kor_nazv
print(my_dict)
otrum_poch_pos = input('Для отримання початкового посилання введіть скорочену назву: ')
for elem in my_dict:
    if otrum_poch_pos in elem:
        print(elem)