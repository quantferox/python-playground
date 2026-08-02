# print("str")
# print(3)
# print(10.5)
# print(0)

# a = 10
# b = 5
# print(a+b)

# a = "str 1"
# b = "str 2"
# print(a, b, sep="||", end="$")

# a = b = c = 777
# stringText = "str"
# arr = []
# numFloat = 0.5

# print(a, b, c)
# print(type(a))  # int
# print(type(stringText))  # str
# print(type(arr))  # list
# print(type(numFloat))  # float
# print(id(a), id(b), id(c))


# Допустимые типы форматирования в пайтон например :.2f и т.п(интерполяция и форматирование)
# типы экранизации и литералы экранизации:
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
# print("\"")
# print("\\")
# print("\rdfgfdgdfgdf\n\rsdfsdfdsfdsfds")
# print("\002")
# print(0x16)
# ==============================================================================
# val = 905677522
# print(f"{val:.2f}") #90.57
# print(f"{val:08.2f}") #00090.57
# print(f"{val:.3%}")
# print(f"{val:,.2f}")
# print(f"{'Hi':x>10}")
# ==============================================================================
# def print_color(text, /, *, R, G, B):
#     print(f"\033[38;2;{R};{G};{B}m\033[48;2;0;0;255m{text:^5}\033[0m")

# print_color("red", R=255, G=0, B=0)

# a = 10
# b = 20
# c = a + b
# d = a + c
# e = a + b + d + c
# print(e)
# a = 10
# b = 20

# def core():
#     global a
#     a = 100
#     return a + b

# print(core())


# print(ord("a"))
# ==============================================================================

# Задача 1: Чётные числа
# Напиши программу, которая создаёт новый список, содержащий все чётные числа из исходного списка чисел от 1 до 20.
# numbers = range(1, 21)
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# numbers = range(1, 21)
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

# Задача 2: Список квадратов чисел
# Используя list comprehension, создай новый список, который содержит квадраты чисел из списка от 1 до 10.
# numbers = range(1, 11)
# Ожидаемый результат: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# numbers = range(1, 11)
# pow_numbers = [x**2 for x in numbers]
# print(pow_numbers)

# Задача 3: Фильтрация по длине строки
# Есть список строк. Используя list comprehension, создай новый список, в котором будут только те строки, длина которых больше 5 символов.
# Пример:
# words = ["apple", "banana", "cherry", "kiwi", "mango", "blueberry"]
# Ожидаемый результат: ['banana', 'cherry', 'blueberry']

# words = ["apple", "banana", "cherry", "kiwi", "mango", "blueberry"]
# normalize_words = [word for word in words if len(word) > 5]
# print(normalize_words)