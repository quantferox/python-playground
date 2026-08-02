# Вопросы
# Базовые задачи
# Создай массив numbers с элементами [10, 20, 30, 40]. Выведи второй элемент массива.
""" numbers = [10, 20, 30, 40]
print(numbers[1]) """

# Добавь число 50 в конец массива numbers и выведи обновленный массив.
""" numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers) """

# Удали элемент с индексом 2 из массива numbers и выведи обновленный массив.
""" numbers = [10, 20, 30, 40, 50]
del numbers[2]
print(numbers) """

# Используй метод len() для вывода длины массива numbers.
""" numbers = [10, 20, 40, 50]
print(len(numbers)) """

# Средний уровень
# Напиши цикл, который выведет квадраты всех чисел в массиве numbers.
""" numbers = [10, 20, 40, 50] """
""" for i in numbers:
    print(i**2) """

""" numbers = [i**2 for i in numbers] """

""" print(list(map(lambda x: x**2, numbers))) """

# Добавь сразу несколько элементов [60, 70, 80] в конец массива numbers, используя метод extend(), и выведи обновленный массив.
""" numbers = [10, 20, 40, 50]
numbers.extend([60,70,80])
print(numbers) """

# Найди индекс элемента 40 в массиве numbers и выведи его.
""" numbers = [10, 20, 40, 50]
print(numbers.index(40)) """

# Сложные задачи
# Отсортируй массив numbers в обратном порядке и выведи его.
""" numbers = [10, 20, 40, 50]
print(sorted(numbers, reverse=True)) """

# Напиши функцию, которая принимает массив и возвращает новый массив, содержащий только четные числа из исходного.
""" numbers = [10, 20, 40, 50]
def odd_arr_value(numbers):
    # numbers = numbers.copy()
    numbers = [i for i in numbers if i % 2 == 0]
    return numbers
print(id(numbers)) #unique
print(id(odd_arr_value(numbers))) #unique """

# Напиши программу, которая удаляет все элементы из массива, которые встречаются больше одного раза. Например:
# Вход: [10, 20, 20, 30, 40, 40, 50]
# Выход: [10, 30, 50].
""" numbers = [10, 20, 20, 30, 40, 40, 50]
numbers = [i for i in numbers if numbers.count(i) == 1]
print(numbers) """

# Экспертный уровень
# Напиши программу, которая принимает два массива и возвращает новый массив, содержащий только те элементы, которые есть в обоих массивах (пересечение).
""" numbers_one = [1, 2, 3, 4, 5]
numbers_two = [3, 4, 5, 6, 7]
intersection_numbers = list(set(numbers_one) & set(numbers_two))
print(intersection_numbers) """

# Напиши программу, которая находит второй по величине элемент в массиве.
# Пример входа: [20, 10, 40, 30, 50]
# Выход: 40.
""" numbers = [20, 10, 40, 30, 50]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers[1]) """

""" numbers = [20, 10, 40, 30, 50]
current_max_value = float("-inf")
previous_max_value = float("-inf")

for number in numbers:
    if number > current_max_value:
        previous_max_value = current_max_value
        current_max_value = number
print(previous_max_value) """