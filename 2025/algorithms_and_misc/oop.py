from abc import ABC, abstractmethod


# Интерфейс класса
class IInterface(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Абстракция и инкапсуляция
# Скрытие деталей реализации в абстракции (например, методы drive и stop скрывают детали того, как именно это работает)
class Car(IInterface):
    def __init__(self, brand, model, color, max_speed):
        # Приватные атрибуты
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__max_speed = max_speed

    # Приватный метод
    def __calculate_fuel_efficiency(self):
        return self.__max_speed * 0.1

    # Публичные методы
    def drive(self):
        print(f"{self.__brand} {self.__model} is driving at {self.__max_speed} km/h")

    def stop(self):
        print(f"{self.__brand} {self.__model} has stopped.")

    # Переопределение методов
    def __str__(self):
        return f"{self.__brand} {self.__model} - {self.__color}, max speed: {self.__max_speed} km/h"

    def __del__(self):
        print(f"Clearing car object: {self.__brand} {self.__model}")


# Наследование и полиморфизм
class ElectricCar(Car):
    def __init__(self, brand, model, color, max_speed, battery_capacity):
        super().__init__(brand, model, color, max_speed)
        self.battery_capacity = battery_capacity

    def drive(self):
        print(f"{self.__str__()} is driving silently at {self.__max_speed} km/h.")

    def stop(self):
        print(f"{self.__str__()} is stopping using regenerative braking.")

    def charge(self):
        print(f"{self.__str__()} is charging with {self.battery_capacity} kWh.")


# Использование статических и классовых методов
class CarFactory:
    @staticmethod
    def create_car(brand, model, color, max_speed):
        return Car(brand, model, color, max_speed)

    @classmethod
    def create_electric_car(cls, brand, model, color, max_speed, battery_capacity):
        return ElectricCar(brand, model, color, max_speed, battery_capacity)


# Множественное наследование
class Vehicle:
    def start_engine(self):
        print("Starting the engine...")

class ElectricVehicle:
    def charge_battery(self):
        print("Charging battery...")

class ElectricCarWithEngine(ElectricCar, Vehicle):
    pass


# Применение принципов SOLID
class CarWithFuelEfficiency(Car):
    def __init__(self, brand, model, color, max_speed):
        super().__init__(brand, model, color, max_speed)
        self.__fuel_efficiency = self.__calculate_fuel_efficiency()

    def get_fuel_efficiency(self):
        return self.__fuel_efficiency


# Пример использования
car1 = CarFactory.create_car("Toyota", "Corolla", "Red", 180)
car1.drive()
car1.stop()
print(car1)

electric_car = CarFactory.create_electric_car("Tesla", "Model S", "Black", 250, 100)
electric_car.drive()
electric_car.stop()
electric_car.charge()

electric_car_with_engine = ElectricCarWithEngine("Tesla", "Model X", "Blue", 200, 85)
electric_car_with_engine.start_engine()
electric_car_with_engine.charge_battery()
electric_car_with_engine.drive()
