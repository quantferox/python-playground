# Задачи:
# Создание функции и её вызов
# Напиши функцию greet(), которая выводит строку "Привет, мир!". Вызови эту функцию.
""" def greet():
    print("Привет, мир!")
greet() """

# Использование аргументов
# Напиши функцию add(a, b), которая принимает два числа и возвращает их сумму. Вызови функцию с разными аргументами и выведи результат.
""" def add(a,b):
    return a+b
print(add(1,2)) #3
print(add(3,64)) #67
print(add(71,43)) #114 """

# Количество аргументов
# Напиши функцию introduce(name, age), которая принимает имя и возраст, а затем выводит строку:
# "Меня зовут {name}, мне {age} лет."
# Попробуй вызвать функцию с одним аргументом и объясни, почему возникает ошибка.
""" def introduce(name, age):
    return f"Меня зовут {name}, мне {age} лет."
introduce("Murad") """
""" Ошибка возникает из за того что вызван с один аргументом а обязательных аргумента 2
соответственно если name , age = 18 было бы так то и ошибок не было.Т.е отсутствует 1 обязательный аргумент age """

# Аргументы с *args
# Напиши функцию find_max(*numbers), которая принимает любое количество чисел и возвращает наибольшее из них.
# Пример:
# print(find_max(1, 5, 8, 3))  # Ожидается: 8
""" def find_max(*numbers):
    return max(numbers)
print(find_max(1, 5, 8, 3)) """

# Аргументы с **kwargs
# Напиши функцию person_info(**info), которая принимает словарь с информацией о человеке и выводит строку:
# "Имя: {name}, Возраст: {age}", если эти ключи есть в словаре.
# Пример:
# person_info(name="Анна", age=25, city="Москва")
# # Ожидается: "Имя: Анна, Возраст: 25"
""" def person_info(**info):
    print(f"Имя: {info['name']}, Возраст: {info['age']}")
person_info(name="Анна", age=25, city="Москва")  """
""" info.get("name") #так тоже можно получить ключи """

# Параметры по умолчанию
# Напиши функцию greet_user(name="гость"), которая приветствует пользователя. Если имя не передано, выводит: "Привет, гость!".
# Пример:
# greet_user("Алексей")  # Ожидается: "Привет, Алексей!"
# greet_user()           # Ожидается: "Привет, гость!"
""" def greet_user(name="гость"):
    if name:
        print(f"Привет, {name}!")
    else:
        print("Привет, гость!")
greet_user("Алексей")
greet_user()         """

# Передача списка в функцию
# Напиши функцию count_even(numbers), которая принимает список чисел и возвращает количество четных чисел в нём.
# Пример:
# print(count_even([1, 2, 3, 4, 5, 6]))  # Ожидается: 3
""" def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count """

""" def count_even(numbers):
    return len([i for i in numbers if i % 2 == 0])
print(count_even([1, 2, 3, 4, 5, 6])) """

# Рекурсия
# Напиши функцию factorial(n), которая с помощью рекурсии возвращает факториал числа n.
# Пример:
# print(factorial(5))  # Ожидается: 120
""" def factorial(n):
    return n * factorial(n - 1) if n != 1 else 1
print(factorial(5)) """

# Позиционные и только ключевые аргументы
# Напиши функцию calculate(a, b, /, *, operation="add"), которая принимает два числа и строку operation.
# Если operation равна "add", возвращает сумму чисел, если "multiply" — произведение.
# Пример:
# print(calculate(2, 3, operation="add"))      # Ожидается: 5
# print(calculate(2, 3, operation="multiply"))  # Ожидается: 6
""" def calculate(a,b,/,*,operation="add"):
    match operation:
        case "add":
            return a + b
        case "multiply":
            return a*b
        case _:
            return "operation does not exit"
print(calculate(2, 3, operation="add"))
print(calculate(2, 3, operation="multiply")) """

# Объединение всех типов аргументов
# Напиши функцию order_summary(name, /, *items, address, **details), которая выводит:

# Имя покупателя,
# Список заказанных товаров,
# Адрес доставки,
# Остальные детали (например, способ оплаты).
# Пример:
# order_summary(
#     "Анна",
#     "яблоки", "бананы", "молоко",
#     address="ул. Пушкина, д. 10",
#     payment="карта",
#     delivery_time="утро"
# )
# Ожидаемый результат:
# Покупатель: Анна
# Заказ: яблоки, бананы, молоко
# Адрес доставки: ул. Пушкина, д. 10
# Остальные детали: {'payment': 'карта', 'delivery_time': 'утро'}
""" def order_summary(name,/,*items, address, **details):
    print(f"Покупатель: {name}\nЗаказ: {', '.join(items)}\nАдрес доставки: {address}\nОстальные детали: {details}")
order_summary("Анна","яблоки", "бананы", "молоко",address="ул. Пушкина, д. 10",payment="карта",delivery_time="утро") """
