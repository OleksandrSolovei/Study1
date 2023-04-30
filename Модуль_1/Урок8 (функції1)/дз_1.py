def pruvitannia(name='Alex'):
    print('Hello, ', name,'!', sep='')

user_name = input('Введіть імя: ')
if user_name:
    pruvitannia(user_name)
else:
    pruvitannia()