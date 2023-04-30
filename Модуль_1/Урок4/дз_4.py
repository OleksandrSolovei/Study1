a = 1
b = 10
total = 0
for i in range(a, b + 1):
    total = total + i
    ser_arufm = total / b
    # print(int(ser_arufm))
    if i % ser_arufm == 0:
        print(i)
    else:
        continue
#







# for x in range(a, b + 1):
#     if x % ser_arufm == 0:
#         print(x)
#     else:
#         continue



