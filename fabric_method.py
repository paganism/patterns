"""
Wiki
Фабричный метод (Factory Method) - порождающий паттерн для создания объектов различных типов одним интерфейсом.
Плюсы:	Создание объектов, независимо от их типов и сложности процесса создания.
Минусы:	Даже для одного объекта необходимо создать соответствующую фабрику, что увеличивает код.
Описан в Design Patterns.
Фабричный метод (англ. Factory Method также известен как Виртуальный конструктор (англ. Virtual Constructor)) — порождающий шаблон проектирования,
предоставляющий подклассам (дочерним классам) интерфейс для создания экземпляров некоторого класса.
В момент создания наследники могут определить, какой класс создавать.
Иными словами, данный шаблон делегирует создание объектов наследникам родительского класса.
Это позволяет использовать в коде программы не специфические классы, а манипулировать абстрактными объектами на более высоком уровне.
"""

class Doc:
    def show(self):
        raise NotImplementedError()


class LibreDoc(Doc):
    def show(self):
        print('Libre office document format')


class MSDoc(Doc):
    def show(self):
        print('Microsofd document format')


class PDFDoc(Doc):
    def show(self):
        print('PDF document')
        
# fabric method
class App:
    def create_doc(self, type):
        raise NotImplementedError()


class MyApp(App):
    def create_doc(self, type):
        if type == 'xlsx':
            return MSDoc()
        elif type == 'ods':
            return LibreDoc()
        elif type == 'pdf':
            return PDFDoc()


app = MyApp()
app.create_doc('xlsx').show() # Microsofd document format
app.create_doc('ods').show()  # Libre office document format
app.create_doc('pdf').show()  # PDF document
