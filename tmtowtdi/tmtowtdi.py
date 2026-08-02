# 🔧 Задача: Фильтрация и группировка пользователей
# У тебя есть список словарей с данными пользователей:

users = [
    {"name": "Alice", "age": 25, "city": "Baku"},
    {"name": "Bob", "age": 17, "city": "Ganja"},
    {"name": "Charlie", "age": 30, "city": "Baku"},
    {"name": "Diana", "age": 16, "city": "Ganja"},
    {"name": "Eli", "age": 19, "city": "Baku"},
]

# 📝 Задание:
# Отфильтруй только совершеннолетних пользователей (возраст 18+).

adult_users = [user for user in users if user["age"] >= 18]

# Сгруппируй их по городам.
all_cities = {user["city"] for user in users}
result = {city: [] for city in all_cities}
for user in adult_users:
    result[user["city"]].append(user["name"])
for city, names in result.items():
    print(f"{city}: {names}")


# Выведи результат в виде:
# Baku: ['Alice', 'Charlie', 'Eli']
# Ganja: []
