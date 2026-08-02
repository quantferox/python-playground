# # Базовый класс без применения LSP (Liskov Substitution Principle)
# class Bird:
#     def fly(self):
#         print("Flying!")


# class Duck(Bird):
#     pass


# class Penguin(Bird):
#     def fly(self):
#         print("I can't fly!")


# def let_it_fly(bird: Bird):
#     bird.fly()


# # 🔴 Вопрос:
# # Нарушает ли кто-то принцип Лисков? Если да — кто и почему?
# # Да нарушает...Bird т.к он уже реализован и безопасно подставить в наследуемые
# # классы не получится...и нарушение происходит такое что Duck летает а Penguin
# # его поведение переопределяет и получается что один летает а другой нет хотя
# # класс Bird явно реализован и все птицы должны летать


# # Как переделать код, чтобы соблюдался LSP?
# # Базовый класс с применением OCP (Open-Closed Principle)
# from abc import ABC, abstractmethod


# class Bird:
#     def eat(self):
#         print("Pecking food")


# class FlyingBird(Bird):
#     @abstractmethod
#     def fly(self):
#         pass


# class Duck(FlyingBird):
#     def fly(self):
#         print("Flying!")


# class Penguin(Bird):
#     def swim(self):
#         print("Swimming!")


# def let_it_fly(bird: FlyingBird):
#     bird.fly()
