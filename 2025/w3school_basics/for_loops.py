# Уровень 1: Базовые
# Напиши цикл for, который выведет числа от 1 до 10.
""" for i in range(11):
    print(i) """

# Выведи все элементы списка numbers = [10, 20, 30, 40, 50] через цикл for.
""" numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num) """

# Используя цикл for, выведи все символы строки "Python is fun!" по одному на каждой строке.
""" words = "Python is fun!"
for word in words:
    print(word) """

# Уровень 2: Немного сложнее
# Напиши цикл for, который вычисляет сумму всех чисел от 1 до 100 включительно.
""" sum_number = 0
for i in range(1,101):
    sum_number += i
print(sum_number) """

""" sum_number = sum([i for i in range(1,101)])
print(sum_number) """


# Используй цикл for для вывода всех чётных чисел в диапазоне от 1 до 50.
""" for i in range(1,51):
    if i % 2 == 0:
        print(i) """

""" for i in range(1,51):
    if i % 2 != 0:
        continue
    print(i) """

""" for i in range(2,51,2):
    print(i) """

# Напиши программу, которая выводит все элементы словаря с помощью for. Например:
# data = {"name": "Alice", "age": 25, "city": "New York"}
# Программа должна вывести:
# name: Alice
# age: 25
# city: New York

""" datas = {"name": "Alice", "age": 25, "city": "New York"}
for key,value in datas.items():
    print(f"{key}: {value}") """

# Уровень 3: Сложные
# Напиши программу, которая выводит таблицу умножения для чисел от 1 до 5.
# Пример вывода для числа 2:
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20

""" for x in range(1,10):
    for y in range(1,10):
        print(f"{x} x {y} = {x*y}") """

# чисто по приколу
""" print([f"{x} x {y} = {x*y}" for x in range(1, 10) for y in range(1, 10)]) """


# Напиши программу, которая печатает только уникальные элементы списка, используя цикл for.
# Пример: для списка [1, 2, 2, 3, 4, 4, 5] программа должна вывести: 1, 2, 3, 4, 5.

""" elements = [1, 2, 2, 3, 4, 4, 5]
for element in set(elements):
    print(element) """

# Уровень 4: Для разминки мозга
# Дана строка "hello world". Напиши программу, которая использует for, чтобы посчитать количество каждой буквы (игнорируя пробелы). Результат должен быть в виде словаря:
# {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}

""" words = "hello world" """
""" datas = {x:words.count(x) for x in words.replace(" ","")}
print(datas) """

""" datas = {}
for x in words.replace(" ",""):
    datas.update({x: words.count(x)})
print(datas) """

# Используй вложенные циклы for, чтобы вывести все возможные комбинации чисел от 1 до 3:
# Пример:
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 1)
# ...
# (3, 3)

""" for x in range(1, 4):
    for y in range(1, 4):
        print((x, y)) """

# Напиши программу, которая использует цикл for для проверки, является ли строка палиндромом. Например, "racecar" — палиндром, а "hello" — нет.

""" def is_polindrom(word):
    word_reversed = ""
    for i in range(len(word)):
        word_reversed += word[len(word) - i - 1]
    return word_reversed == word

print(is_polindrom("racecar")) """
