"""
Abstract factory (Kit), абстрактная фабрика - паттерн, порождающий объекты.
Предоставляет интерфейс для создания семейств взаимосвязанных или взаимозависимых объектов,
не специфицируя их конкретных классов.
Шаблон реализуется созданием абстрактного класса Factory, который представляет собой интерфейс
для создания компонентов системы (например, для оконного интерфейса он может создавать окна и кнопки).
Затем пишутся классы, реализующие этот интерфейс.
Классы абстрактной фабрики часто реализуются фабричными методами,
но могут быть реализованы и с помощью паттерна прототип.
"""

class AbstractFactory:
    def create_window(self):
        raise NotImplementedError()

    def create_button(self):
        raise NotImplementedError()


class Window:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Button:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_window(self):
        return Window('Big Window')

    def create_button(self):
        return Button('Big Button')


class ConcreteFactory2(AbstractFactory):
    def create_window(self):
        return Window('Small Window')

    def create_button(self):
        return Button('Small Button')

def get_factory(num):
    if num == 0:
        return ConcreteFactory1()
    elif num == 1:
        return ConcreteFactory2()


factory = get_factory(1)
print(factory.create_window())
print(factory.create_button())


factory = get_factory(0)
print(factory.create_window())
print(factory.create_button())
