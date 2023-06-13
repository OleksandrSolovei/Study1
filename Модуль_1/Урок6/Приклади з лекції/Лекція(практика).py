my_list = []
values = input("Введіть 5 значень через пробіл: ").split()
my_list.extend(values)
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list2 = reversed(my_list)


