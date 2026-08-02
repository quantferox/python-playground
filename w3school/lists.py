""" # Исходный список
myList = [
    "lion",     # 0
    "tiger",    # 1
    "elephant", # 2
    "giraffe",  # 3
    "zebra",    # 4
    "panda",    # 5
    "wolf",     # 6
    "kangaroo", # 7
    "fox",      # 8
    "bear",     # 9
]

# 1. extend() добавляет элементы из другого списка или итерации в конец текущего списка
myList.extend(["koala", "leopard"])
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear', 'koala', 'leopard']

# 2. sort() сортирует список в алфавитном порядке (по умолчанию) или по ключу
myList.sort()
print(myList)
# ['bear', 'elephant', 'fox', 'giraffe', 'kangaroo', 'koala', 'leopard', 'lion', 'panda', 'tiger', 'wolf', 'zebra']

# 3. reverse() меняет порядок элементов на обратный
myList.reverse()
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 4. insert() вставляет элемент в указанную позицию
myList.insert(2, "dolphin")
print(myList)
# ['zebra', 'wolf', 'dolphin', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 5. pop() удаляет элемент по индексу и возвращает его
removed_item = myList.pop(2)  # Удаляем элемент с индексом 2
print(removed_item)           # dolphin
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 6. clear() удаляет все элементы из списка
myList.clear()
print(myList)
# []

# Восстанавливаем список для дальнейших примеров
myList = [
    "lion", "tiger", "elephant", "giraffe", "zebra", 
    "panda", "wolf", "kangaroo", "fox", "bear"
]

# 7. copy() создает копию списка
copied_list = myList.copy()
print(copied_list)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']

# 8. index() возвращает индекс первого вхождения указанного элемента
index_of_zebra = myList.index("zebra")
print(index_of_zebra)
# 4

# 9. remove() удаляет первое вхождение указанного элемента
myList.remove("zebra")
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']
 """

""" 
1.Создание списка и вывод
Создай список с элементами "Python", "JavaScript" и "C++". Выведи этот список на экран.
"""
""" myList = ["Python", "JavaScript", "C++"]
print(myList) """

""" 
2.Длина списка
У тебя есть список: 
Напиши код, который выводит количество элементов в этом списке.
"""

""" languages = ["Python", "JavaScript", "C++", "Java", "C#"]
print(len(languages)) """

""" 
3.Обращение по индексу
Используй список из второго задания. Напиши код, который выводит:

Первый элемент списка.
Последний элемент списка. 
"""

""" languages = ["Python", "JavaScript", "C++", "Java", "C#"]
print(languages[0]) #Первый элемент
print(languages[-1]) #Последний элемент
print(languages[len(languages) - 1]) #Последний элемент """

""" 
4.Замена элемента
В списке:
Замени "banana" на "kiwi" и выведи обновлённый список.
"""
""" fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits) """


"""
5.Проверка на существование
В списке:
Проверь, есть ли число 30 в этом списке. Если да, выведи "Found", иначе "Not Found". 
"""

""" numbers = [10, 20, 30, 40, 50]

if 30 in numbers:
    print("Found")
else:
    print("Not Found") """

"""
6.Добавление элемента
В список:
Добавь "hamster" и выведи обновлённый список.
"""

""" animals = ["cat", "dog", "rabbit"]
animals.append("hamster")
print(animals) """

"""
7.Удаление элемента
В списке из шестого задания удали "dog" и выведи результат.
"""

""" animals = ["cat", "dog", "rabbit"]
animals.remove("dog") # variant
animals.pop(1) # variant
del animals[1] # variant """


# Задачи:
"""
1.Список с разными типами данных
Создай список, который содержит следующие элементы: строку "hello", число 42, и булево значение True. 
Выведи этот список и тип его элементов.
"""

""" myList = ["hello", 42, True]
print(myList)

# Типы данных
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))

# Типы данных
print(*(type(elm) for elm in myList)) """


"""
2.Использование list() конструктора
Создай список из строки "banana" с помощью конструктора list(). Выведи результат.
"""

""" myList = list("banana")
myList2 = list(elm for elm in "banana")
print(myList)
 """
"""
3.Дубликаты в списке
У тебя есть список:
Напиши код, который выводит все уникальные элементы списка, сохраняя их порядок.
"""

""" fruits = ["apple", "banana", "apple", "cherry", "cherry"]
fruits_unique = []
for fruit in fruits:
    if fruit not in fruits_unique:
        fruits_unique.append(fruit)
print(fruits_unique) """


"""
4.Добавление нескольких элементов
Есть список:
Добавь в него элементы "yellow" и "purple" за одну операцию. Выведи результат.
"""

""" colors = ["red", "green", "blue"]
colors += ["yellow", "purple"]
colors.extend(["yellow", "purple"])
print(colors) """

"""
5.Удаление всех элементов
Удали все элементы из списка:
И выведи пустой список.
"""

""" numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)
 """


""" 
6.Копирование списка
Создай копию списка:
Убедись, что изменения в копии не влияют на оригинал.
"""

""" names = ["John", "Jane", "Joe"]
names_copy = names.copy()
 """

""" names = ["John", "Jane", "Joe"]
for idx in range(len(names)):
    print(names[idx]) """

""" names = ["John", "Jane", "Joe"]
idx = 0
while idx <= len(names)-1:
    print(names[idx])
    idx += 1 """


# List Comprehension

"""
1. Самое простое:
Создай список квадратов чисел от 0 до 4.

Результат должен быть:
[0, 1, 4, 9, 16]
"""

""" numbers = [squares**2 for squares in range(0, 5)]
print(numbers)
 """

"""
2. Фильтр с условием:
Создай список только чётных чисел из диапазона от 0 до 9.

Результат должен быть:
[0, 2, 4, 6, 8]
"""

""" numbers = [evenNum for evenNum in range(0,10) if evenNum % 2 == 0]
print(numbers)
 """

"""
3. Преобразование с фильтром:
Умножь каждое нечётное число от 1 до 10 на 3.

Результат должен быть:
[3, 9, 15, 21, 27]
"""

""" numbers = [oddNumber*3 for oddNumber in range(1,11) if oddNumber % 2 != 0]
print(numbers) """


"""
4. Сложение строк:
Создай список, где к каждому имени из ['Alice', 'Bob', 'Charlie'] добавлено слово " is awesome!".

Результат должен быть:
['Alice is awesome!', 'Bob is awesome!', 'Charlie is awesome!']
"""

# variant
""" words = ["Alice","Bob","Charlie"]
words = [word + " is awesome!" for word in words]
print(words) """

# variant
""" words = [word + " is awesome!" for word in ["Alice","Bob","Charlie"]]
print(words) """

# больше в голову ничего не пришло как по другому решить если есть способ лучший покажи

"""
5. Работа с вложенными циклами:
Создай список всех пар чисел (x, y) для чисел от 1 до 3, где x меньше y.

Результат должен быть:
[(1, 2), (1, 3), (2, 3)]
"""

# я не уверен правильно ли или нет но результат верный
# задача для первого раза сложная поэтому сначала полная версия кода
""" x = 3
y = 3
number_pairs = []
for val_x in range(1, x + 1):
    for val_y in range(1, y + 1):
        if val_x < val_y:
            number_pairs.append((val_x, val_y))

print(number_pairs) """

# а теперь с помощью генератора списка

""" x = 3
y = 3
number_pairs = [
    (val_x, val_y)
    for val_x in range(1, x + 1)
    for val_y in range(1, y + 1)
    if val_x < val_y
]
print(number_pairs) """


# CONTINUE LEVEL SENIOR :D

"""
1.Объединение строк из вложенных списков
Есть вложенный список строк:

data = [["Alice", "Bob"], ["Charlie", "Dave"], ["Eve"]]
Создай один плоский список, где каждая строка из вложенных списков добавлена с префиксом "Hello, ".

Результат должен быть:
["Hello, Alice", "Hello, Bob", "Hello, Charlie", "Hello, Dave", "Hello, Eve"]
"""

""" data = [["Alice", "Bob"], ["Charlie", "Dave"], ["Eve"]]
nameList = ["Hello, " + name for datas in data for name in datas]
print(nameList) """


"""
2. Квадраты простых чисел
Найди квадраты всех простых чисел от 1 до 50.
Результат должен быть:
[4, 9, 25, 49, 121, 169, ...]  # квадраты простых чисел
Подсказка: Напиши проверку на простое число прямо в List Comprehension.
"""

""" simpleNums = [
    nums**2
    for nums in range(2, 51)
    if all(nums % x != 0 for x in range(2, int(nums**0.5) + 1))
]
print(simpleNums) """


"""
3. Комбинации слов
Есть два списка:
nouns = ["cat", "dog", "car"]
adjectives = ["big", "small", "fast"]
Создай список всех возможных сочетаний вида "adjective noun".

Результат должен быть:
["big cat", "big dog", "big car", "small cat", ..., "fast car"]
"""

""" nouns = ["cat", "dog", "car"]
adjectives = ["big", "small", "fast"]

newList = [f"{x} {y}" for x in adjectives for y in nouns]
print(newList) """


"""
4. Сгруппировать числа по чётности
Дан список чисел:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Создай словарь, где ключи — "even" и "odd", а значения — списки чётных и нечётных чисел соответственно.

Результат должен быть:
{"even": [2, 4, 6, 8, 10], "odd": [1, 3, 5, 7, 9]}
"""

""" numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
collection = {
    "even": [even for even in numbers if even % 2 == 0],
    "odd": [odd for odd in numbers if odd % 2 != 0],
}
print(collection) """


"""
5. Магический квадрат
Создай список кортежей, где каждый кортеж содержит три числа (a, b, c) из диапазона 1–20, таких что их сумма равна 30.
Условие: a <= b <= c (упорядоченные тройки).

Результат должен быть:
[(10, 10, 10), (8, 11, 11), (7, 11, 12), ...]
"""

""" collection = [
    (a, b, c)
    for a in range(1, 21)
    for b in range(1, 21)
    for c in range(1, 21)
    if (a <= b <= c) and (a + b + c == 30)
]
print(collection) """

# adlar = ["Rza", "GPT", "Vagif", "Ayxan", "Aytac", "Murad"]
# if founded target name change current index item list to new name
# adlar = [f"Hello {ad}" if ad.casefold() == "gpt" else f"How are you {ad}" for ad in adlar]


# List Comprehension #ucked :D
# adlar = [
#     (
#         f"Hello {ad}"
#         if ad.casefold() == "gpt"
#         else f"How are you {ad}" if ad.casefold() == "ayxan" else ad
#     )
#     for ad in adlar
# ]


# if "gpt" in map(lambda ad:ad.casefold(),adlar):
#     print("Hello GPT!") #its me :D
# elif "ayxan" in map(lambda ad:ad.casefold(),adlar):
#     print("How are you Ayxan?")
# else:
#     print(":(")

# print(adlar)

# numbers = [1,128,32,64,4,2,8,16]
# numbers.sort()
# numbers.reverse()
# print(numbers)


""" myList = ["Apple","Kiwi","Mango","Banana","Lemon","Lime","Orange"]
print(myList[::3])

slicedListIdx = slice(None,None,3)
print(myList[slicedListIdx]) """

# print("\033[31mThis is red text\[0m")

# a = "string"
# print(a[0].upper() + a[-len(a) + 1 :])
# print(a[0].upper() + a[1:])
# print(a.capitalize())
# print(a.title())

#pip install colorama
# import colorama as col

# print(col.Fore.RED + "ПРИВЕТ" + col.Style.RESET_ALL)
# or
""" print("\033[48;2;46;204;113;38;2;0;0;255mGREEN_TEXT\033[0m") """