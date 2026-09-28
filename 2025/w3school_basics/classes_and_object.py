# Задачи:
# Создание класса и объекта: Напиши класс Car, у которого есть свойство brand (марка автомобиля) со значением "Toyota". Создай объект car1 этого класса и выведи значение свойства brand.
""" class Car():
    def __init__(self):
        self.brand = "Toyota"

car1 = Car()
print(car1.brand) """

# Использование метода __init__: Создай класс Animal, который принимает два параметра в конструкторе: name (имя) и species (вид животного). Создай объект animal1 с именем "Tiger" и видом "Big Cat", и выведи оба свойства.
""" class Animal():
    def __init__(self, name,species):
        self.name = name
        self.species = species
animal1 = Animal("Tiger", "Big Cat")
print(f"Name: {animal1.name}\t Species: {animal1.species}") """

# Добавление метода: В классе Person добавь метод is_adult, который проверяет, является ли возраст (age) объекта больше или равен 18. Верни True или False.
# Пример:
# p1 = Person("Alice", 17)
# print(p1.is_adult())  # Должно вывести False
""" class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p1 = Person("Alice",17)
p2 = Person("Murad",27)
print(p1.is_adult()) #False
print(p2.is_adult()) #True """

# Метод __str__: Создай класс Book с параметрами title (название) и author (автор). Добавь метод __str__, чтобы при печати объекта возвращалась строка вида "Название книги: <title>, Автор: <author>".
# Пример:
# book1 = Book("1984", "George Orwell")
# print(book1)  # Должно вывести: Название книги: 1984, Автор: George Orwell
""" class Book():
    def __init__(self, title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Название книги: {self.title}, Автор: {self.author}"

book1 = Book("1984","George Orwell")
print(book1) """

# Модификация свойства: Создай объект p2 класса Person с именем "Bob" и возрастом 30. Измени возраст объекта на 35 и выведи новое значение свойства age.
""" class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p1 = Person("Bob",30)
print(p1.age) #30
p1.age = 35
print(p1.age) #35 """

# Удаление свойства: В объекте p1 класса Person удали свойство age, а затем попробуй вывести его. Какую ошибку ты получишь?
""" class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p1 = Person("Bob",30)
del p1.age
print(p1.age) # Ошибка будет 'Person' object has no attribute 'age' потому что свойство age больше нет...логично """

# Использование pass: Объясни, зачем может понадобиться использование оператора pass в пустом определении класса.
""" Допустим у нас функция
def func():
И нам пока нужно остановится и перейти к следующей функции
def func1():
Произойдет так что пайтон из за того что читает вместе scope {} пробелы ожидает какую нибудь строку или что то другое
которое выполняется внутри функции и поэтому горит ошибка синтаксиса
Чтобы временно заглушить ошибку используется pass кроме того она нужна чтобы функция просто ничего не выполняла 
и возвращаемый тип у такой функции NoneType -> None
"""
""" def func():
    pass

print(type(func())) """