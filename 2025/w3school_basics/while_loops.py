# Уровень 1: Базовые
# Напиши цикл while, который выведет числа от 1 до 10.
""" x = 1
while x <= 10:
    print(x)
    x += 1 """

# Используй цикл while, чтобы вывести все чётные числа от 2 до 20.
""" x = 2
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1 """

""" x = 2
while x <= 20:
    print(x) if x % 2 == 0 else None
    x += 1 """


# Уровень 2: Немного сложнее
# Напиши программу, которая запрашивает у пользователя ввод чисел через input. Цикл должен завершаться, если пользователь вводит 0. В конце программа должна вывести сумму всех введённых чисел.
""" num_arr = []

while True:
    x = int(input("Enter a number:"))
    num_arr.append(x)
    if x == 0:
        break

print(sum(num_arr)) """

# Напиши цикл while, который выведет первые 10 чисел Фибоначчи (0, 1, 1, 2, 3, 5, ...).
""" i = 0
prev_fibo = 0
curr_fibo = 1

while i < 10:
    print(prev_fibo)
    next_fibo = curr_fibo + prev_fibo
    prev_fibo = curr_fibo
    curr_fibo = next_fibo
    i += 1
 """

# Уровень 3: Сложные
# Напиши цикл while, который будет проверять, является ли число n простым. Если n простое, программа должна вывести n is prime, иначе n is not prime.
""" num = 11
k = 2

while k * k <= num and num % k != 0:
    k += 1
print("is prime") if k * k > num else print("is not prime") """

# Напиши программу, которая с помощью while определяет наибольшую цифру в числе n, введённом пользователем.
""" num = input("Enter a number:")
max_digit_in_num = max([int(i) for i in num])
print(max_digit_in_num) """

# Уровень 4: Для разминки мозга
# Реализуй "угадай число". Программа загадывает случайное число от 1 до 100 (используй random.randint), а пользователь должен его угадать. Программа подсказывает, больше или меньше загаданное число. Цикл завершается, когда число угадано.
""" import random

random_num = random.randint(1, 100)
max_attempts = 10

while max_attempts > 0:
    input_num = int(input("Enter a number:"))
    if input_num > random_num:
        print(f"The number you guessed is less than yours. Attempts:{max_attempts}")
    if input_num < random_num:
        print(f"The number you guessed is greater than yours. Attempts:{max_attempts}")
    if input_num == random_num:
        print(f"You won!")
        break
    max_attempts -= 1
else:
    print(f"Attempts are over! The Hidden Number {random_num}") """


# Напиши программу, которая запрашивает у пользователя строку и переворачивает её (без использования [::-1] или функций вроде reversed). Используй только цикл while.
""" str_input = input("Enter a word:")
str_input_reversed = ""

i = len(str_input) - 1
while i >= 0:
    str_input_reversed += str_input[i]
    i -= 1

print(str_input_reversed) """
