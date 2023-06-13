numeric_1 = input("Введіть число перше: ")
numeric_2 = input("Введіть число друге: ")
if numeric_1.isdigit() and numeric_2.isdigit():
    numeric_1 = int(numeric_1)
    numeric_2 = int(numeric_2)
    if numeric_1 < numeric_2:
        total = 0
        for i in range(numeric_1, numeric_2 + 1, 7):
            total += i
        print(total)
    else:
        print("Перше число має бути менше за друге.")
else:
    print("Некоректні дані. Введіть два числа.")