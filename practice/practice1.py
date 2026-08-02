# ==============================================================================
# Базовый класс-утилита
# ==============================================================================
# 🧪 Задача:
# У тебя есть код:

# class StringUtils:
#     def capitalize_words(self, text):
#         return ' '.join(word.capitalize() for word in text.split())


# class MyLogger(StringUtils):
#     def log(self, message):
#         formatted = self.capitalize_words(message)
#         print(f"[LOG] {formatted}")
# 💥 Найди, в чём тут проблема, и предложи более правильный вариант.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class StringUtils:
#     @staticmethod
#     def capitalize_words(text):
#         return " ".join(word.capitalize() for word in text.split())


# class MyLogger:
#     def log(self, message):
#         formatted = StringUtils.capitalize_words(message)
#         print(f"[LOG] {formatted}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==============================================================================
# Anemic Domain Model
# ==============================================================================
# 💼 Задача: Пользователь и баланс
# У тебя есть вот такой код — класс с чистыми данными и функция, которая работает с ними:


# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance


# def withdraw(user: User, amount: float):
#     if user.balance >= amount:
#         user.balance -= amount
#     else:
#         raise ValueError("Недостаточно средств")


# 📌 Задание:
# Переделай код так, чтобы User стал богатым объектом — со своей логикой снятия денег (withdraw), без внешней функции.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance


#     def withdraw(self, amount: float):
#         if amount > self.balance:
#             raise ValueError("Недостаточно средств")
#         self.balance -= amount
# ==============================================================================
# Вызов предка
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal создан: {self.name}")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.breed = breed
#         print(f"Dog создан: {self.breed}")


# d = Dog("Шарик", "Ovcharka")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal создан: {self.name}")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#         print(f"Dog создан: {self.breed}")


# d = Dog("Шарик", "Ovcharka")
# ==============================================================================
# Ошибка пустого подкласса
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} издаёт звук."


# class Dog(Animal):
#     pass
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} издаёт звук."


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)


#     def speak(self):
#         return f"{self.name} лает: Гав-гав!"
# ==============================================================================
# Божественный объект
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class App:
#     def __init__(self):
#         self.users = []
#         self.settings = {}
#         self.logger = []

#     def add_user(self, user):
#         self.users.append(user)

#     def log(self, message):
#         self.logger.append(message)

#     def get_setting(self, key):
#         return self.settings.get(key)

#     def set_setting(self, key, value):
#         self.settings[key] = value


#     def send_email(self, to, subject, body):
#         print(f"Отправка письма {to}: {subject}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class User:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class Logging:
    def __init__(self):
        self.logger = []

    def log(self, message):
        self.logger.append(message)


class Setting:
    def __init__(self):
        self.settings = {}

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        self.settings[key] = value


class Email:
    @staticmethod
    def send_email(to, subject, body):
        print(f"Отправка письма {to}: {subject}")


# ==============================================================================
# Объектная клоака
# class SharedState:
#     def __init__(self):
#         self.data = {}


# class ComponentA:
#     def do_something(self, state: SharedState):
#         state.data["a"] = "something from A"


# class ComponentB:
#     def do_something(self, state: SharedState):
#         print(state.data.get("a"))
# ==============================================================================
# class SharedState:
#     def __init__(self):
#         self._data = {}

#     def set_value(self, key, value):
#         self._data[key] = value

#     def get_value(self, key):
#         return self._data.get(key)


# class ComponentA:
#     def do_something(self, state: SharedState):
#         state.set_value("a", "something from A")


# class ComponentB:
#     def do_something(self, state: SharedState):
#         value = state.get_value("a")
#         print(value)
# ==============================================================================
# Полтергейст

# class Engine:
#     def start(self):
#         print("Двигатель запущен")

# class Car:
#     def __init__(self, engine):
#         self.engine = engine

#     def start_engine(self):
#         self.engine.start()

# class CarController:
#     def __init__(self, car):
#         self.car = car


#     def start(self):
#         self.car.start_engine()
# ==============================================================================
# class Engine:
#     def start_engine(self):
#         print("Двигатель запущен")


# class Car(Engine):
#     pass
# ==============================================================================
# Проблема йо-йо
# ==============================================================================
# class Entity:
#     def update(self):
#         print("Обновление сущности")


# class MovingEntity(Entity):
#     def update(self):
#         super().update()
#         print("Обновление движения")


# class AnimatedMovingEntity(MovingEntity):
#     def update(self):
#         super().update()
#         print("Обновление анимации")


# class Player(AnimatedMovingEntity):
#     def update(self):
#         super().update()
#         print("Обновление игрока")
# ==============================================================================
# class Entity:
#     def update(self):
#         print("Обновление сущности")


# class MovingEntity(Entity):
#     def update(self):
#         super().update()
#         print("Обновление движения")


# class AnimatedMovingEntity(Entity):
#     def update(self):
#         super().update()
#         print("Обновление анимации")


# class Player(Entity):
#     def update(self):
#         super().update()
#         print("Обновление игрока")
# ==============================================================================
# Одиночество
# ==============================================================================
# class Address:
#     def __init__(self, street, city):
#         self.street = street
#         self.city = city


# class Order:
#     def __init__(self, id, total):
#         self.id = id
#         self.total = total
# ==============================================================================
# class Address:
#     def __init__(self, street, city):
#         self._street = street
#         self._city = city

#     def __str__(self):
#         return f"{self._street}, {self._city}"

#     @property
#     def street(self):
#         return self._street

#     @street.setter
#     def street(self, value):
#         self._street = value

#     @property
#     def city(self):
#         return self._city

#     @city.setter
#     def city(self, value):
#         self._city = value


# class Order:
#     def __init__(self, id, total, address: Address):
#         self._id = id
#         self._total = total
#         self._address = address


#     def __str__(self):
#         return f"Order #{self._id} — Total: {self._total}, Ship to: {self._address}"
# ==============================================================================
# Френд-зона
# ==============================================================================
# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance


# class AccountManager:
#     def withdraw_all(self, account: BankAccount):
#         print(f"Снято {account._balance}₽")
#         account._balance = 0
# ==============================================================================
# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         self._balance = value

#     def withdraw_all(self):
#         amount = self._balance
#         self._balance = 0
#         return amount


# class AccountManager:
#     def withdraw_all(self, account: BankAccount):
#         amount = account.withdraw_all()
#         print(f"Снято {amount}₽")
# ==============================================================================
# Каша из интерфейсов
# ==============================================================================
# class Printer:
#     def print_text(self, text):
#         print(text)

#     def print_image(self, image):
#         print(f"Печать изображения {image}")

#     def print_pdf(self, pdf):
#         print(f"Печать PDF {pdf}")

#     def scan_document(self, doc):
#         print(f"Сканирование {doc}")


#     def fax_document(self, doc):
#         print(f"Отправка факса {doc}")
# ==============================================================================
# class Printer:
#     @staticmethod
#     def print_text(text):
#         print(text)

#     @staticmethod
#     def print_image(image):
#         print(f"Печать изображения {image}")

#     @staticmethod
#     def print_pdf(pdf):
#         print(f"Печать PDF {pdf}")


# class Scanner:
#     @staticmethod
#     def scan_document(doc):
#         print(f"Сканирование {doc}")


# class Faxxer:
#     @staticmethod
#     def fax_document(doc):
#         print(f"Отправка факса {doc}")
# ==============================================================================
# Висящие концы
# ==============================================================================
# class UserManager:
#     def __init__(self):
#         self.users = []

#     def add_user(self, user):
#         self.users.append(user)

#     def remove_user(self, user):
#         self.users.remove(user)


#     def deactivate_user(self, user):
#         # ??? Тут пока нет реализации
#         pass
# ==============================================================================
# class UserManager:
#     def __init__(self):
#         self.users = []

#     def add_user(self, user):
#         self.users.append(user)


#     def remove_user(self, user):
#         self.users.remove(user)
# ==============================================================================
# Заглушка
# ==============================================================================
# class PaymentProcessor:
#     def process_payment(self, amount):
#         # TODO: Реализовать метод
#         pass
# ==============================================================================
# class PaymentProcessor:
#     def process_payment(self, amount):
#         return f"Платёж на сумму {amount} обработан (заглушка)"
# ==============================================================================
