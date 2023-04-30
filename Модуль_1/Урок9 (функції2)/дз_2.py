word = input('Введіть слово: ')
if word == word[::-1]:
    print('Паліндром!')
else:
    print('Не паліндром!')