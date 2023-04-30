pib = input('Введіть ПІБ: ').split()
if len(pib) == 3:
    for i in pib:
        if not i.isalpha() or not i.istitle():
            print('Ви ввели некоректні дані!')
            break
        else:
            print(i)
else:
    print('Ви ввели некоректні дані!')