day = input('Введіть день тижня: ').title()
match day:
    case 'Понеділок' | 'Вівторок' | 'Середа' | 'Четвер' | 'Пятниця':
        print(day + ' - будній день.')
    case 'Субота' | 'Неділя':
        print(day + ' - вихідний день.')
    case _:
        print('Такого дня тижня не існує.')