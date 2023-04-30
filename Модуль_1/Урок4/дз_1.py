from builtins import input

a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))

tot = 0
for d in range(a, b + 1):
    tot = tot + d
print(tot)
