"""домашнє завдання 10.4"""

def add_tovaru(store):
    """функція додає нові товари в магазин"""

    tovar = input('Вкажіть назву товара: ').split(",")
    my_tuple = tuple(x for x in tovar)
    store.insert(0, my_tuple)


store = []
kil_tovariv = int(input('Вкажіть скільки товарів буде додано: '))
for i in range(kil_tovariv):
    add_tovaru(store)
print(store)
