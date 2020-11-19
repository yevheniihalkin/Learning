# Задание 1: У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число

value = 77
new_value = value / 2 if value < 100 else -value
print(new_value)

#####################################################®
# Задание 2: У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0

value = 156
new_value = 1 if value < 100 else 0
print(new_value)

#####################################################
# Задание 3: У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False

value = 76
new_value = True if value < 100 else False
print(new_value)

#####################################################
# Задание 4: У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.

my_str = "Hello, my name is Eugene"
my_str = my_str.upper()
print(my_str)

#####################################################
# Задание 5: У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.

my_str = "Hello, my name is Eugene"
my_str = my_str.lower()
print(my_str)

#####################################################
# Задание 6: У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.

my_str = "Hell"
if len(my_str) < 5:
    my_str = 2 * my_str
    print(my_str)
else:
    my_str
    print(my_str)

#####################################################
# Задание 7: У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.

my_str = "Hi"
if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
    print(my_str)
else:
    my_str
    print(my_str)

#####################################################
# Задание 8: У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.

my_str = 'Hello, my name is Eugene. I was born in June 1996!'
new_str = ''
for symbol in my_str:
    if symbol.isalnum():
        new_str += symbol
print(new_str)

#####################################################
# Задание 9: У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.

my_str = 'Hello, my name is Eugene. I was born in June 1996!'
new_str = ''
for symbol in my_str:
    if not symbol.isalnum():
        new_str += symbol
print(new_str)

#####################################################
# Задание 10: У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.

my_str = 'Hello, my name is Eugene. I was born in June 1996!'
new_str = ''
for symbol in my_str:
    if not symbol.isalnum() and symbol != ' ':
        new_str += symbol
print(new_str)