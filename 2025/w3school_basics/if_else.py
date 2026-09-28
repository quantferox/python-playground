# Уровень 1: Базовые

# Напиши сокращённый if else, чтобы переменная result получила значение 'positive', если число в переменной num больше 0, иначе 'negative or zero'.
""" num = 9
result = "positive" if num > 0 else "negative or zero"
result = "positive" if num > 0 else "negative" if num < 0 else "zero"
print(result) """

# Используя shorthand if, выведи It's even, если число в переменной num делится на 2 без остатка.
""" num = 8
print("It's even") if num % 2 == 0 else print("It's odd") """

# Уровень 2: Немного сложнее
# Используя сокращённый if else, присвой переменной message значение:
# 'adult', если возраст age больше или равен 18,
# 'minor' в противном случае.
""" age = 17
message = "adult" if age >= 18 else "minor" 
print(message) """


# Используя сокращённый if-elif-else, присвой переменной grade значения:
# 'A', если score больше или равен 90,
# 'B', если score от 70 до 89,
# 'C' в остальных случаях.
""" score = 20
grade = "A" if score >= 90 else "B" if score >= 70 and score <= 89 else "C"
print(grade) """


# Уровень 3: Сложные
# Используя вложенные сокращённые условия, присвой переменной result значение:
# 'hot', если temperature больше 30,
# 'warm', если temperature от 15 до 30,
# 'cold', если temperature меньше 15.
""" temperature = -5
result = "hot" if temperature >= 30 else "warm" if temperature >=15 and temperature <= 30 else "cold"
print(result)
 """

# Присвой переменной output значение 'even and positive', если число n больше 0 и чётное; 'odd', если оно нечётное, и 'zero', если равно 0.
""" n = 2
output = "even and positive" if n > 0 and n % 2 == 0 else "odd" if n % 2 != 0 else "zero" if n == 0 else None
print(output) """

# Уровень 4: Для разминки мозга
# Дана переменная x. Присвой переменной result значение:
# 'divisible by 3 and 5', если x делится на 3 и на 5,
# 'divisible by 3', если делится только на 3,
# 'divisible by 5', если делится только на 5,
# 'not divisible by 3 or 5' в остальных случаях.
""" x = 36
is_devide_three = True if sum([int(i) for i in str(x)]) % 3 == 0 else False
is_devide_five = True if x % 10 == 5 or x % 10 == 0 else False
is_devide_three_five = is_devide_three and is_devide_five
result = (
    "divisible by 3 and 5"
    if is_devide_three_five
    else (
        "divisible by 3"
        if is_devide_three
        else "divisible by 5" if is_devide_five else "not divisible by 3 or 5"
    )
)
print(result) """