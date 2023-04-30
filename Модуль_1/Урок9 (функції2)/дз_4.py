def snch(n):
    if n == 0:
        return 0
    return n + snch(n - 1)

my_ran = int(input('Введіть число: '))
print(snch(my_ran))

