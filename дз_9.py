#1Светофор
import time

class TrafficLight:
    __color = 'красный'

    def running(self):
        print(self.__color)
        self.__color = 'желтый'
        time.sleep(7)
        print(self.__color)
        self.__color = 'зеленый'
        time.sleep(2)
        print(self.__color)
        time.sleep(5)

a = TrafficLight()
a.running()
d = TrafficLight()
d.running()

#2
class Road:

    def __init__(self, length, width):
        self._length= length
        self._width= width

    def mass(self, weight, thick):
        mass = self._length*self._width*weight*thick
        print(f'Масса асфальта для покрытия дороги = {mass} т.')

a = Road(200, 300)
a.mass(25, 5)
print(a._length)

#3
class Worker:
    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income= income

class Position(Worker):
    def __init__(self, name, surname, position, **income):
        super().__init__(name, surname, position, **income)
    def get_full_name(self):
        print(f'Полное имя - {self.name} {self.surname}')
    def get_total_income(self):
        total_income = 0
        for val in self._income.values():
            total_income += val
        print('Общий доход ', total_income)

a = Worker('Leo', 'Smirnov', 'director', оклад=100000, премия=20000)
print(a.name, a.surname, a.position, a._income)

a = Position('Leo', 'Smirnov', 'director', оклад=100000, премия=20000)
a.get_full_name()
a.get_total_income()

b =Position('Kate', 'Middleton', 'princess', оклад=50000, премия=0)
b.get_total_income()
b.get_full_name()
print(b.name, b.surname, b.position, b._income)

#4
class Car:
    def __init__(self, speed, color, name, is_polise):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_polise = is_polise

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула на {direction}')
    def show_speed(self):
        print('Скорость ', self.speed)
class TownCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)
        self.is_polise = False
    def show_speed(self):
        if self.speed>60:
            print('Превышение скорости')
        else:
            print('Скорость ', self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        if self.speed >40:
            print('Превышение скорости')
        else: print('Скорость ', self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

a = TownCar(62, 'black', 'Nissan', False)
b = SportCar(120, 'red', 'Ferrari', False)
c = WorkCar(60, 'white', 'Audi', False)
d = PoliceCar(80, 'blue', 'Lada', True)

for x in [a, b, c, d]:
    print(x.name, x.speed, x.color, x.is_polise)
    x.go()
    x.stop()
    x.turn('лево')
    x.show_speed()

#5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Написали', self.title)

class Pensil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Начертили', self.title)

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Раскрасили', self.title)

a = Stationery('дом')
a.draw()
a= Pen('дом')
a.draw()
a = Pensil('дом')
a.draw()
a= Handle('дом')
a.draw()