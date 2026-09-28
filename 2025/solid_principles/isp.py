# # Базовый класс без применения ISP (Interface Segregation Principle)
# # Представь, у тебя есть интерфейс Document:
# from abc import ABC, abstractmethod


# class Document(ABC):
#     @abstractmethod
#     def print(self): ...

#     @abstractmethod
#     def scan(self): ...

#     @abstractmethod
#     def fax(self): ...


# # Базовый класс с применения ISP (Interface Segregation Principle)
# # Представь OldPrinter, который умеет только печатать.
# class Printable(ABC):
#     @abstractmethod
#     def print(self): ...


# class Scanable(ABC):
#     @abstractmethod
#     def scan(self): ...


# class Faxable(ABC):
#     @abstractmethod
#     def fax(self): ...


# class OldPrinter(Printable):
#     def print(self):
#         print("Printing document...")


# class SmartPrinter(Printable, Scanable, Faxable):
#     def print(self):
#         print("Printing...")

#     def scan(self):
#         print("Scanning...")

#     def fax(self):
#         print("Faxing...")
# ==============================================================================
# # 🔴 Задача: Что не так?
# from abc import ABC, abstractmethod


# class Worker(ABC):
#     @abstractmethod
#     def work(self): ...

#     @abstractmethod
#     def eat(self): ...


# class HumanWorker(Worker):
#     def work(self):
#         print("Working hard!")

#     def eat(self):
#         print("Having lunch!")


# class RobotWorker(Worker):
#     def work(self):
#         print("Executing tasks")

#     def eat(self):
#         raise NotImplementedError("Robots don't eat!")


# # ✅ Вопрос 1:
# # Что нарушено?
# # Нарушено реализация и наследования Worker человек может кушать а вот робот нет
# # Каким принципом SOLID? Почему?
# # solId - ISP отсутствует разделение интерфейсов

# # ✅ Вопрос 2:
# # Как переделать этот код, чтобы соблюдался ISP?
# from abc import ABC, abstractmethod


# class Workable(ABC):
#     @abstractmethod
#     def work(self): ...


# class Eatable(ABC):
#     @abstractmethod
#     def eat(self): ...


# class HumanWorker(Workable, Eatable):
#     def work(self):
#         print("Working hard!")

#     def eat(self):
#         print("Having lunch!")


# class RobotWorker(Workable):
#     def work(self):
#         print("Executing tasks")
