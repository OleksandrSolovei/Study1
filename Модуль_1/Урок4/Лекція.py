# import turtle
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(50)
# turtle.forward(100)
# turtle.exitonclick()

a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
tot = 0
while a >= b:
    print('Перше число має бути менше за друге!')
    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))
else:
    for i in range(a, b + 1, 7):
        tot += i
    print('Сума =', tot)
