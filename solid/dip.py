# Базовый класс без применения DIP (Dependency Inversion Principle)
# class MySQLDatabase:
#     def save(self, data):
#         print(f"Saving {data} to MySQL")


# class ReportService:
#     def __init__(self):
#         self.db = MySQLDatabase()

#     def generate(self, data):
#         print("Generating report...")
#         self.db.save(data)


# Базовый класс с применения DIP (Dependency Inversion Principle)
# from abc import ABC, abstractmethod


# class DatabaseService(ABC):
#     @abstractmethod
#     def save(self): ...


# class MySQLDatabase(DatabaseService):
#     def save(self, data):
#         print(f"Saving {data} to MySQL")


# class ReportService:
#     def __init__(self, db_service: DatabaseService):
#         self.db = db_service

#     def generate(self, data):
#         print("Generating report...")
#         self.db.save(data)
