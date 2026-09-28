def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Перед вызовом функции делаем что то")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper


@my_decorator
def func():
    print("it's so easy")

func()