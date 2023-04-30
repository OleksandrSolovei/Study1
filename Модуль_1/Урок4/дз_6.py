for i in range(3):
    login = input('Введіть логін:')
    parol = input('Введіть пароль:')
    if login == 'log' and parol == 'par':
        print('Вхід виконано!')
        break
    else:
        print('Логін або пароль введено невірно.')
else:
    print('Перевищено ліміт спроб на вхід! Спробуйте пізніше!')






