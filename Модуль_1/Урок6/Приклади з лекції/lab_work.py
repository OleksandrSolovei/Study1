from dis import dis
from timeit import timeit
import random
from matplotlib import pyplot as plt

print(dis('data_one = []'))
print(dis('data_one = list()'))
print(dis('data_one = [1, 2, 3]'))

y = (2, 4, 8, 12, 16, 20, 24, 28, 32)
x1 = [
    timeit('data_one = [1, 2]'),
    timeit('data_one = [1, 2, 3, 4]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,'
           ' 26, 27, 28]'),
    timeit('data_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,'
           ' 26, 27, 28, 29, 30, 31, 32]')
]

x2 = [
    timeit('data_two = list((1, 2))'),
    timeit('data_two = list((1, 2, 3, 4))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))'),
    timeit('data_two = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,'
           ' 26, 27, 28))'),
    timeit('data_one = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,'
           ' 26, 27, 28, 29, 30, 31, 32))')
]

plt.plot(y, x1, y, x2)
plt.legend(('[]', 'list()'))
plt.show()

N = 24
data_one = [i for i in range(N)]
data_two = list(range(N))
data_three = [*range(N)]
print(data_one == data_two == data_three)

N = 24
MIN = -100_000
MAX = 10_000_000
test_data_one = (random.randint(MIN, MAX) for _ in range(N))
test_data_two = (random.randint(MIN, MAX) for _ in range(N))
data_one = [*test_data_one]
data_two = list(test_data_two)

"""
При роботі зі списками використання квадратних дужок не тільки заощаджує натискання клавіш на клавіатурі, але й часто 
показує кращі результати швидкодії. Втім, це лише мільйонні частки секунди. Для найпростіших завдань різницю складно 
помітити. Але якщо звикли працювати зі списком через дужки, думка про економію тактів процесора грітиме вам душу.
"""