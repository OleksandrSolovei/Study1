# знайти найменше значення, найбільше, суму всіх значень, середнє арифметичне
from statistics import mean
my_list = [2, 1, 6, 8, 8]
print(max(my_list))
print(min(my_list))
total = 0
for i in my_list:
    total += i
print(total)
ser = mean(my_list)
print(ser)

