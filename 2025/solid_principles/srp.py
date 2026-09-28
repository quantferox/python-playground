# Базовый класс без применением SRP (Single Responsibility Principle)
# class Car:
#     def __init__(self, brand, model, engine_type, hp, is_hybrid):
#         self._brand = brand
#         self._model = model
#         self._engine_type = engine_type
#         self._hp = hp
#         self._is_hybrid = is_hybrid

#     def brand(self):
#         print(f"Brand: {self._brand}")

#     def model(self):
#         print(f"Model: {self._model}")

#     def engine_type(self):
#         print(f"Engine type: {self._engine_type}")

#     def hp(self):
#         print(f"Horsepower: {self._hp} HP")

#     def is_hybrid(self):
#         print(f"Is hybrid: {self._hybrid}")

#     def save_to_database(self):
#         print(f"Saving {self._brand} {self._model} to database...")

#     def load_from_file(self):
#         print("Loading car data from file...")

#     def render_on_screen(self):
#         print(f"Rendering {self._brand} {self._model} on screen...")

#     def calculate_tax(self):
#         tax = 150 if self._hybrid else 300
#         print(f"Calculated tax: ${tax}")

#     def send_email_to_owner(self):
#         print(f"Sending email to owner about {self._brand} {self._model}...")

#     def log_car_info(self):
#         print(
#             f"[LOG] {self._brand} {self._model} - {self._engine_type} - {self._hp} HP"
#         )

#     def start_engine(self):
#         print(f"{self._brand} {self._model}'s engine started.")

#     def stop_engine(self):
#         print(f"{self._brand} {self._model}'s engine stopped.")

#     def perform_diagnostics(self):
#         print(f"Running diagnostics on {self._brand} {self._model}...")


# Базовый класс с применением SRP (Single Responsibility Principle)
# class CarService:
#     def __init__(self, brand, model):
#         self._brand = brand
#         self._model = model

#     def brand(self):
#         print(f"Brand: {self._brand}")

#     def model(self):
#         print(f"Model: {self._model}")


# class EngineService:
#     def __init__(self, engine_type, hp, is_hybrid):
#         self._engine_type = engine_type
#         self._hp = hp
#         self._is_hybrid = is_hybrid

#     def engine_type(self):
#         print(f"Engine type: {self._engine_type}")

#     def hp(self):
#         print(f"Horsepower: {self._hp} HP")

#     def is_hybrid(self):
#         print(f"Is hybrid: {self._is_hybrid}")

#     def start_engine(self):
#         print(f"Engine started.")

#     def stop_engine(self):
#         print(f"Engine stopped.")


# class DatabaseService:
#     def save_to_database(self, car_service: CarService):
#         print(
#             f"Saving {car_service._brand} {car_service._model} to database..."
#         )


# class FileService:
#     def load_from_file(self):
#         print("Loading car data from file...")


# class MailService:
#     def send_email_to_owner(self, car_service: CarService):
#         print(
#             f"Sending email to owner about {car_service._brand} {car_service._model}..."
#         )


# class LoggerService:
#     def log_car_info(
#         self, car_service: CarService, engine_service: EngineService
#     ):
#         print(
#             f"[LOG] {car_service._brand} {car_service._model} - {engine_service._engine_type} - {engine_service._hp} HP"
#         )


# class RenderService:
#     def render_on_screen(self, car_service: CarService):
#         print(
#             f"Rendering {car_service._brand} {car_service._model} on screen..."
#         )


# class CalculateService:
#     def calculate_tax(self, engine_service: EngineService):
#         tax = 150 if engine_service.is_hybrid else 300
#         print(f"Calculated tax: ${tax}")


# class DiagnosticsService:
#     def perform_diagnostics(self, car_service: CarService):
#         print(
#             f"Running diagnostics on {car_service._brand} {car_service._model}..."
#         )


# ==============================================================================
# DTO Example:
# class CarDTO:
#     def __init__(self, brand, model, engine_type, hp, is_hybrid):
#         self.brand = brand
#         self.model = model
#         self.engine_type = engine_type
#         self.hp = hp
#         self.is_hybrid = is_hybrid


# class CarRenderService:
#     def render(self, car: CarDTO):
#         print(f"Rendering {car.brand} {car.model} on screen...")


# car_data = CarDTO("Toyota", "Camry", "Hybrid", 200, True)
# renderer = CarRenderService()
# renderer.render(car_data)
