#1
import datetime
import re
class Date:
    def __init__(self, date):
        self.date = date
    @classmethod
    def numbers(cls, date):
        try:
            day, month, year = re.split(r'[-,.,:]', date)
            return int(day), int(month), int(year)
        except:
            print('Неверно указан разделитель')
            exit()
    @staticmethod
    def check(date):
        day = date[0]
        month = date[1]
        year = date[2]
        try:
            datetime.date(year, month, day)
            print(f'Дата указана верно')
        except ValueError:
            print(f'Дата указана неверно')

wrong_date = '29.02.2001'
birthday = '23-12-1993'
print(Date.numbers(wrong_date))
print(Date.numbers(birthday))
Date.check(Date.numbers(wrong_date))
Date.check(Date.numbers(birthday))

#2
import sys
class Error:
    @classmethod
    def div_num(self, num1, num2):
        try:
            print(num1 // num2)
        except ZeroDivisionError:
            print('Деление на ноль. Введите другое число')

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])
Error.div_num(num_1, num_2)

#3
import re
class Check_nums:
    @classmethod
    def nums_list(self):
        nums_list = []
        while True:
            num = input('Введите число ')
            if num == 'stop':
                print(nums_list)
                exit()
            if re.match(r'^\d+.\d+$', num):
                nums_list.append(float(num))
            elif re.match(r'^\d+$', num):
                nums_list.append(int(num))
            else:
                print('Не число! Попробуйте ещё раз')

Check_nums.nums_list()

#4,5,6
class Storehouse:
    store_house = {'Принтер':{}, 'Сканер': {}, 'Ксерокс':{}}
    @classmethod
    def get_equipment(cls, equip, count):
        try:
            count = int(count)
        except ValueError:
            print(count, '- не является числом!')
            exit()
        val = cls.store_house.get(equip.__str__(), None)
        if val is not None:
            val_count = val.get((equip.name, f'Speed={equip.speed}'))
            if (val_count is not None):
                val_count+= count
                cls.store_house[equip.__str__()][(equip.name, f'Speed={equip.speed}')] = val_count
            else:
                cls.store_house[equip.__str__()][(equip.name, f'Speed={equip.speed}')]= count
        print(cls.store_house)

    @classmethod
    def give_away(cls, equip, count):
        val = cls.store_house.get(equip.__str__())
        if val.get((equip.name, f'Speed={equip.speed}'), None) is not None:
            val_count = val.get((equip.name, f'Speed={equip.speed}'))
            if val_count>= count:
                cls.store_house[equip.__str__()][(equip.name, f'Speed={equip.speed}')]-=count
                if cls.store_house[equip.__str__()][(equip.name, f'Speed={equip.speed}')] == 0:
                    del cls.store_house[equip.__str__()][(equip.name, f'Speed={equip.speed}')]
                    print('Оборудование закончилось ')
            else: print('На складе только ', val_count, 'шт')
        else:
            print( 'На складе нет такого оборудования')
        print(cls.store_house)

class Of_equipment:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Printer(Of_equipment):
    def __init__(self, name, color, speed):
        super(Printer, self).__init__(name, speed)
        self.color = color

    def __str__(self):
        return 'Принтер'

class Scanner(Of_equipment):
    def __init__(self, name, format, speed):
        super(Scanner, self).__init__(name, speed)
        self.format = format

    def __str__(self):
        return 'Сканер'

class Copier(Of_equipment):
    def __init__(self, name, dpi, speed, wifi):
        super(Copier, self).__init__(name, speed)
        self.dpi = dpi
        self.wifi = wifi

    def __str__(self):
        return 'Ксерокс'

p_1 = Printer('Canon', color=False, speed=30)
p_2 = Printer('HP', True, 10)
s_1 = Scanner('HP', 'A4', 10)
c_1 = Copier('ACER', 250, 20, True)

print(p_1.name, s_1.format, c_1.wifi)

Storehouse.get_equipment(p_1, '5')
Storehouse.get_equipment(s_1, 2)
Storehouse.get_equipment(c_1, 3)
#Storehouse.get_equipment(p_1, 3)
#Storehouse.get_equipment(p_2, 1)
Storehouse.give_away(p_1, 2)
Storehouse.give_away(p_1, 3)
Storehouse.give_away(s_1, 3)
Storehouse.give_away(c_1, 3)
Storehouse.give_away(p_2, 1)

#7 Комплексные числа
import re
class Complex_num:
    def __init__(self, num):
        try:
            num_a, num_b = re.findall(r'\d+|[+-]\d+', num)
            self.num_a = int(num_a)
            self.num_b = int(num_b)
        except ValueError:
            num_a, num_b = re.findall(r'\d+|[+-]', num)
            num_b += '1'
            self.num_a = int(num_a)
            self.num_b = int(num_b)
    def __add__(self, other):
        return f'{self.num_a + other.num_a} + {self.num_b + other.num_b}i'
    def __mul__(self, other):
        return f'{self.num_a*other.num_a - self.num_b*other.num_b} +{self.num_a * other.num_b + self.num_b * other.num_a}i'

x = Complex_num('3+2i')
y= Complex_num('2-i')
print(x+y)
print(x*y)