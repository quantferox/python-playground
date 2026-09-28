# 🧩 Задача: нарушен ли KISS?
# Перед тобой код backend-функции для расчёта стоимости доставки:


# class DeliveryOption:
#     def __init__(self, option):
#         self.option = option

#     def calculate(self, weight):
#         if self.option == "standard":
#             return weight * 1.2 + 5
#         elif self.option == "express":
#             return weight * 2.0 + 10
#         elif self.option == "overnight":
#             return weight * 3.0 + 20
#         else:
#             raise ValueError("Invalid delivery option")


# 💭 Кажется простым? Но представь, таких "опций" станет 10+, или они хранятся в БД, или передаются из JSON-а.


# ✅ Вопрос 1:
# Что тут нарушает KISS?
# Попробуй сам сформулировать.
# Если option опции станут больше +10 if конструкция будет разрастраться что усложнит функцию
# и соответственно нарушит KISS
# 💡 Подсказка Всё поведение запихнуто в один `if`-блок, усложняя код. Добавление новых опций требует изменения `calculate`.
# ✅ Вопрос 2:
# Как бы ты переписал этот код по принципу KISS — просто, без перегибов, но гибко?
# 2 Часа ночи в голову только пришла мысль sOlid буква O

# from abc import ABC, abstractmethod


# class DeliveryOption(ABC):
#     @abstractmethod
#     def calculate(self, weight): ...


# class StandartDeliveryOption(DeliveryOption):
#     def calculate(self, weight):
#         return weight * 1.2 + 5


# class ExpressDeliveryOption(DeliveryOption):
#     def calculate(self, weight):
#         return weight * 2.0 + 10


# class OvernightDeliveryOption(DeliveryOption):
#     def calculate(self, weight):
#         return weight * 3.0 + 20


# class DeliveryCalculator:
#     def calculate(self, weight, delivery_option: DeliveryOption):
#         return delivery_option.calculate(weight)


# ==============================================================================
# DELIVERY_PRICES = {
#     "standard": lambda w: w * 1.2 + 5,
#     "express": lambda w: w * 2.0 + 10,
#     "overnight": lambda w: w * 3.0 + 20,
# }


# def calculate_delivery(weight, option):
#     try:
#         return DELIVERY_PRICES[option](weight)
#     except KeyError:
#         raise ValueError("Invalid delivery option")
