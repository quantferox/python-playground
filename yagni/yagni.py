# 🧩 Задача: нарушен ли YAGNI?
# Представь, ты работаешь над системой управления заказами в e-commerce. Вот код, написанный твоим коллегой:
# class Order:
#     def __init__(self, id, items):
#         self.id = id
#         self.items = items
#         self.status = "new"

#     def calculate_total(self):
#         return sum(item["price"] * item["quantity"] for item in self.items)

#     def cancel(self):
#         self.status = "cancelled"

#     def print_invoice(self):
#         print("Invoice for order", self.id)
#         for item in self.items:
#             print(f"- {item['name']} x{item['quantity']}")
#         print("Total:", self.calculate_total())

#     def estimate_shipping_date(self):
#         return "3-5 business days"

#     def send_sms_notification(self, message):
#         print(f"Sending SMS to customer: {message}")

#     def generate_gift_wrapping_instructions(self):
#         return "Wrap each item with red ribbon"


# ✅ Вопросы к тебе:
# Какие методы ты бы заподозрил как нарушение YAGNI?
# estimate_shipping_date - send_sms_notification - generate_gift_wrapping_instructions
# Почему именно они?
# Ну скорее всего лишние потому что главный функционал это вычеслить стоимость
# и произвести оплату + реализовать отмену остальное второстепенное


# Как можно исправить этот класс с учётом YAGNI?
# class Order:
#     def __init__(self, id, items):
#         self.id = id
#         self.items = items
#         self.status = "new"

#     def calculate_total(self):
#         return sum(item["price"] * item["quantity"] for item in self.items)

#     def cancel(self):
#         self.status = "cancelled"

#     def print_invoice(self):
#         print("Invoice for order", self.id)
#         for item in self.items:
#             print(f"- {item['name']} x{item['quantity']}")
#         print("Total:", self.calculate_total())
