def introspection_info(obj):
    info = {}

    # Получение типа объекта
    info['type'] = str(type(obj)).split("'")[1]

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Получение модуля, к которому принадлежит объект
    info['module'] = obj.__module__

    # Другие интересные свойства (например, длина, если объект имеет длину)
    if hasattr(obj, '__len__'):
        info['length'] = len(obj)

    return info

class SampleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


# Создание объекта класса
sample_obj = SampleClass("Alice")

# Интроспекция объекта
info = introspection_info(sample_obj)
print(info)