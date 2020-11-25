# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [1, 4, 6, 7, 9, 120, 500]
for item in my_list:
    if item > 100:
        print(item)

#####################################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [1, 4, 6, 7, 9, 120, 500]
my_results = []

for item in my_list:
    if item > 100:
        my_results.append(item)

print(my_results)

#####################################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [1, 4, 6, 7, 9, 120, 500]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-2] + my_list [-1])

print(my_list)

#####################################################

# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.

value = input("Введи число в формате десятичной дроби: ")

try:
    value = float(value)
    result = value ** -1
    print(result)

except ZeroDivisionError:
    print("Division by zero is forbidden")
except ValueError:
    print("This value isn't a digit")

# #####################################################

# 5) У вас есть список значений my_list и список индексов my_indexes
# (начинается с нуля и количество элементов совпадает с количеством в my_list.
# Распечатать значения из my_list через обращение по индексу. См. пример выше.

my_list = ["Eugene", "Ann", "Olga", "Stacia", "Bogdan"]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
	print(my_list[index])

# #####################################################

# 6) У вас есть два списка my_list_1 и my_list_2 равной длинны и
# список индексов my_indexes (начинается с нуля и количество элементов
# совпадает с количеством в my_list_1.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу.


my_list_1 = ["One", "Two", "Three"]
my_list_2 = ["Un", "Deux", "Trois"]
my_indexes = [0, 1, 2]
result = ()

for index in my_indexes:
	print(my_list_1[index], my_list_2[index])

# #####################################################

# 7) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.

my_string = '0123456789'
my_list = []

for number in my_string:
    for number_copy in my_string:
        result = int(number + number_copy)
        my_list.append(result)

print(my_list)