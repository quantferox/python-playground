# 🔧 ЗАДАЧА: "Отчёты по продажам" (WET-код)
# У тебя есть код, который обрабатывает месячные отчёты по продажам для разных регионов. Сейчас всё написано через копипасту.
# Задание: перепиши это по принципу DRY, выделив общую логику.

# def report_north(sales):
#     total = 0
#     for s in sales:
#         if s["region"] == "north":
#             total += s["amount"]
#     print(f"North region: {total}$")


# def report_south(sales):
#     total = 0
#     for s in sales:
#         if s["region"] == "south":
#             total += s["amount"]
#     print(f"South region: {total}$")


# def report_east(sales):
#     total = 0
#     for s in sales:
#         if s["region"] == "east":
#             total += s["amount"]
#     print(f"East region: {total}$")


# def report_west(sales):
#     total = 0
#     for s in sales:
#         if s["region"] == "west":
#             total += s["amount"]
#     print(f"West region: {total}$")

# 🔍 Условия:
# sales — список словарей, у каждого region и amount.
# Твоя задача — убрать дублирование, но сохранить поведение.
# Подумай над расширяемостью: чтобы потом не пришлось снова копировать код, если появится central.
# Если хочешь — могу потом проверить твой DRY-ответ или дать подобную задачу, но с валидацией формы или с HTML/JS.


# def report_region(sales, region):
#     total = 0
#     for s in sales:
#         if s["region"] == region:
#             total += s["amount"]
#     print(f"{region.capitalize()} region: {total}$")
