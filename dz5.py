# Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
            print('«Запуск отрисовки»')

class Pen(Stationery):
    def draw(self):
        print('«Запуск отрисовки». Пишим ручкой!')

class Pencil(Stationery):
    def draw(self):
        print('«Запуск отрисовки». Пишим карандашем!')

class Handle(Stationery):
    def draw(self):
        print('«Запуск отрисовки». Пишим маркером!')

pen = Pen('Ручка')
print(pen)
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()