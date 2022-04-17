# задание 4
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poliсe = is_police

    def go(self):
        print('автомобиль движется')
    def stop(self):
        print('автомобиль остановился')
    def turn(self, direction):
        print(f'автомобиль повернул на {direction}')
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ВНИМАНИЕ: ПРИВЫШЕНИЕ СКОРОСТИ!')
        print(f'скорость автомобиля {self.speed}')

class SportCar(Car):
        pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('ВНИМАНИЕ: ПРИВЫШЕНИЕ СКОРОСТИ!')
        print(f'скорость автомобиля {self.speed}')
class PoliceCar(Car):
        pass


# town_car = TownCar(70, 'цвет: Серебро', 'AUDI A3', False)
# town_car.show_speed()
# sport_car = SportCar(110, 'цвет: Красный', 'NISSAN 350Z', False)
# sport_car.turn('Право')
# work_car = WorkCar(41, 'цвет: Красный', 'Трактор', False)
# work_car.go()
police_car = PoliceCar(431, 'цвет: Хаки', 'Bugatti Veyron Super Sport ', True)
police_car.go()
police_car.show_speed()