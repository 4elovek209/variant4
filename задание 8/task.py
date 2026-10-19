import functools
import inspect

def validate_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = inspect.signature(func).bind(*args, **kwargs)
            bound.apply_defaults()
            names = list(bound.arguments)
            for i in range(len(types)):
                value = bound.arguments[names[i]]
                if not isinstance(value, types[i]):
                    raise TypeError(f"{names[i]} должен быть {types[i].__name__}, пришло {type(value).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    """Складывает два числа"""
    return a + b

@validate_types(str)
def greet(name):
    """Приветствует по имени"""
    return "Привет, " + name

@validate_types(int)
def total(first, *rest):
    """Суммирует первое число и хвост"""
    s = first
    for x in rest:
        s += x
    return s

print(add(2, 3))
print(add(a=2, b=5))
print(greet("Анна"))
print(total(1, 2, 3, 4))
print(add.__name__, add.__doc__)
try:
    print(add(2, "3"))
except TypeError as e:
    print("Ошибка:", e)
