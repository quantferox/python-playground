# from abc import ABC, abstractmethod


# # Базовый класс без применения OCP (Open-Closed Principle)
# class DiscountCalculator:
#     def calculate(self, customer_type: str, amount: float) -> float:
#         if customer_type == "regular":
#             return amount * 0.9
#         elif customer_type == "vip":
#             return amount * 0.8
#         elif customer_type == "student":
#             return amount * 0.85
#         else:
#             return amount


# # Базовый класс с применением OCP (Open-Closed Principle)
# class DiscountCalculator(ABC):
#     @abstractmethod
#     def calculate(self, amount: float) -> float:
#         return amount


# class RegularCalculator(DiscountCalculator):
#     def calculate(self, amount: float) -> float:
#         return amount * 0.9


# class VipCalculator(DiscountCalculator):
#     def calculate(self, amount: float) -> float:
#         return amount * 0.8


# class StudentCalculator(DiscountCalculator):
#     def calculate(self, amount: float) -> float:
#         return amount * 0.85
