"""
Singleton (Одиночка) - это паттерн, который порождает объекты.
Одиночка гарантирует, что класс имеет только один инстанс (экземпляр) и предоставляет к нему доступ.
С помощью этого паттерна можно реализовать паттерны, такие как абстрактная фабрика, строитель, прототип.
Также в python возможно создать отдельный модуль, а потом просто его импортировать. Это также будет являться одиночкой.
"""

class Singleton:
    __instance = None

    @staticmethod
    def inst():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __init__(self):
        print("Constructor called!")

a = Singleton.inst()
b = Singleton.inst()
print('a is {}, \nb is {}, \na is b == {}'.format(a, b, (a is b)))
