""" a = """ """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it
"""
""" 
a = "Hello, World!" """

""" print(a[0])
print(a[1])
print(a[2])
"""
""" 
for idx in a:
    print(idx) """

""" print(len(a)) """

""" if "hello" in a.lower():
    print("Found!")
else:
    print("Not Found!") """

""" if "hello" in a.lower():
    print("Found!")
elif "hello" not in a.lower():
    print("Not Found!") """

""" b = "   Hello, World   " """
# print(b[2:5]) # llo
# print(b[:5]) #Hello
# print(b[2:]) #llo, World
# print(b[-5:-2]) #Wor
# print(b[1::2]) #Hello,Wprld => el

# print(b.upper())
# print(b.lower())
# print(b.strip()) #trim
# print(b.lstrip()) #trim left
# print(b.rstrip()) #trim right

# b = "Hello, World"
# print(b.replace("H","J"))
# print("-".join(b.split(",")))
# print("<=>".join(b.split(",")))
# print("|".join(b.strip() for b in b.split(",")))


# print("Hello " + "World " + "I " + "am " + "Murad") # :D

""" b = "Hello {}, how are you?"
print(b.format("Murad")) """

# print(f"Hello {'Murad'} how are you?")

""" price = 59.432 """

""" print(f"This is macbook, price {price:.1f}") """


# STRING METHODS

""" a = "hello, world"
b = "Hello, World"
c = "123456" """

# b[0] = "1" #TypeError: 'str' object does not support item assignment

# print(a.capitalize())
# print(b.center(len(b) + 10,"*")) #fill
# print(a.count("o")) #includes count
# print(a.title())
# print(a.isupper())
# print(a.islower())
# print(c.isdigit())
# print(a.istitle())
# print(a.replace("hello", "Hi"))
# print(a.startswith("hello"))
# print(a.endswith("stop"))

""" a = "-54"
print(a.zfill(10))
print(isinstance(a, int)) """

""" a = "HelloWorld"
print(a[::-1])
print(id(a)) """

""" a = "HelloWorld"
print(a.encode(encoding="windows-1251", errors="backslashreplace")) """

"""(STRING METHODS LIST) CHAT GPT GENERATE: """

# isalnum() - Проверяет, что строка состоит только из букв и цифр
print("Python3".isalnum())    # True: только буквы и цифры
print("Python 3".isalnum())   # False: есть пробел
print("12345".isalnum())      # True: только цифры
print("Hello!".isalnum())     # False: есть "!"

# isalpha() - Проверяет, что строка состоит только из букв
print("Python".isalpha())     # True: только буквы
print("Python3".isalpha())    # False: есть цифра
print("Hello!".isalpha())     # False: есть "!"
print("".isalpha())           # False: пустая строка

# isascii() - Проверяет, что строка содержит только ASCII-символы
print("Hello".isascii())      # True: только ASCII-символы
print("123!".isascii())       # True: цифры и спецсимволы из ASCII
print("Привет".isascii())     # False: кириллица не входит в ASCII
print("".isascii())           # True: пустая строка тоже считается ASCII

# isdecimal() - Проверяет, что строка содержит только десятичные цифры
print("12345".isdecimal())    # True: только десятичные цифры
print("１２３４５".isdecimal()) # True: цифры в формате Юникода
print("123.45".isdecimal())   # False: точка не является цифрой
print("".isdecimal())         # False: пустая строка

# isdigit() - Проверяет, что строка состоит только из цифр
print("12345".isdigit())      # True: только цифры
print("²³".isdigit())         # True: верхние индексы
print("123.45".isdigit())     # False: точка не цифра
print("".isdigit())           # False: пустая строка

# isidentifier() - Проверяет, что строка является допустимым идентификатором
print("variable".isidentifier())   # True: валидный идентификатор
print("2variable".isidentifier())  # False: начинается с цифры
print("var-iable".isidentifier())  # False: дефис не разрешен
print("_variable".isidentifier())  # True: начинается с "_"

# isnumeric() - Проверяет, что строка содержит числовые значения
print("12345".isnumeric())    # True: только цифры
print("½".isnumeric())        # True: дробь
print("²³".isnumeric())       # True: верхние индексы
print("123.45".isnumeric())   # False: точка не является числом

# isprintable() - Проверяет, что все символы строки печатные
print("Hello, World!".isprintable())  # True: все символы печатные
print("Hello\nWorld".isprintable())   # False: "\n" не печатный символ
print("".isprintable())               # True: пустая строка считается печатной

# expandtabs() заменяет табуляции на пробелы
print("Hello\tWorld".expandtabs())        # Hello   World (по умолчанию 8 пробелов)
print("Hello\tWorld".expandtabs(4))      # Hello   World (4 пробела)
print("123\t456\t789".expandtabs(2))     # 123  456  789 (2 пробела)

# find() ищет подстроку и возвращает индекс первого вхождения (или -1, если не найдено)
print("Hello, World!".find("World"))     # 7: "World" начинается с 7-го индекса
print("Hello, World!".find("Python"))    # -1: подстрока не найдена
print("Hello, World!".find("o", 5, 10))  # 8: "o" найдено между индексами 5 и 10

# format() вставляет значения в строку (позиционные и именованные аргументы)
print("My name is {0} and I am {1} years old.".format("John", 25))  
# My name is John and I am 25 years old.
print("I live in {city}, {country}.".format(city="Baku", country="Azerbaijan"))
# I live in Baku, Azerbaijan.

# format_map() вставляет значения из словаря
info = {"name": "John", "age": 25}
print("My name is {name} and I am {age} years old.".format_map(info))  
# My name is John and I am 25 years old.

# index() ищет подстроку и возвращает индекс первого вхождения (ошибка, если не найдено)
print("Hello, World!".index("World"))    # 7: "World" начинается с 7-го индекса
# print("Hello, World!".index("Python")) # Ошибка: подстрока не найдена

# maketrans() и translate() для замены символов
table = str.maketrans("aeiou", "12345")  # Создаем таблицу для замены гласных на цифры
print("hello world".translate(table))    # h2ll4 w4rld (замена гласных на цифры)

# partition() разбивает строку на 3 части: до, совпадение, после
print("I love Python".partition("love"))  # ('I ', 'love', ' Python')
print("I love Python".partition("Java"))  # ('I love Python', '', '')

# rfind() ищет подстроку и возвращает индекс последнего вхождения (или -1, если не найдено)
print("Hello, World!".rfind("o"))        # 8: последний "o" найден на 8-м индексе
print("Hello, World!".rfind("Python"))   # -1: подстрока не найдена

# rindex() ищет подстроку и возвращает индекс последнего вхождения (ошибка, если не найдено)
print("Hello, World!".rindex("o"))       # 8: последний "o" найден на 8-м индексе
# print("Hello, World!".rindex("Python")) # Ошибка: подстрока не найдена

# rpartition() разбивает строку на 3 части: до, последнее совпадение, после
print("I love Python and Python loves me".rpartition("Python"))  
# ('I love Python and ', 'Python', ' loves me')

# splitlines() разбивает строку по символам перевода строки и возвращает список
print("Line1\nLine2\nLine3".splitlines())            # ['Line1', 'Line2', 'Line3']
print("Line1\nLine2\nLine3".splitlines(True))        # ['Line1\n', 'Line2\n', 'Line3']

# translate() заменяет символы на основе таблицы перевода
table = str.maketrans("abc", "123")  # Таблица для замены: a -> 1, b -> 2, c -> 3
print("abcd".translate(table))      # 123d (a, b, c заменены, d осталась)
