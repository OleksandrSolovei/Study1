string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Поділ рядка поелементний, при цьому створюється список
print(string.split())

print(string.strip())
print(string.count('s'))
print(string.replace('Lorem', 'LOREM'))

print(str(len(string)).isdigit())
print(string.title())
print(string.capitalize()) # перше слово з великої літери
print(string.lower())
print(string.upper())
print(string.center(100, '+')) # 100 - максимальна кількість символів в рядку
my_char = ord(string[0]) # код символу
print(my_char)
print(chr(my_char)) # перетворює код символу в літеру
print('\nstring'.isspace())    # превіряє чи є пробіли
print(string.startswith('L'))  # чи починається із якогось символу
print(string.endswith('.'))    # чи закінчується на символ
print('string'.isalpha())      # в рядку тільки літери
print(string.casefold())       # генерування регістру
