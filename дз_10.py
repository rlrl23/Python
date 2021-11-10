#1
class Matrix:
    def __init__(self, *matrix):
        self.matrix = matrix[0]

    def __str__(self):
        line = ''
        for i in range(0, len(self.matrix[0])):
            for elem in self.matrix:
                line += f'{elem[i]}   '
            line += '\n'
        return line

    def __add__(self, other):
        if len(self.matrix)==len(other.matrix) and len(self.matrix[0])==len(other.matrix[0]):
            return [[x+y for x,y in zip(row_1, row_2)] for row_1, row_2 in zip(self.matrix, other.matrix)]
        else:
            print('Размер матриц должен быть одинаковым!')

a =Matrix([[31,37,51], [22,43,86]])
print(a)
b =Matrix([[1,2,3], [0,1,1]])
print(a+b)

# 2
from abc import ABC, abstractmethod
class AbsractClass(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def sum_cloth(self):
        pass
class Clothes(AbsractClass):
    def __init__(self, *args):
        self.args = list(args)
    @property
    def sum_cloth(self):
        total_sum = 0
        for arg in self.args:
            total_sum += arg.sum_cloth()
        return (round(total_sum, 2))

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def sum_cloth(self):
        return round(self.size / 6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def sum_cloth(self):
        return (self.height * 2 + 0.3)

a = Coat(44)
b = Suit(100)
print(a.sum_cloth(), b.sum_cloth())
c = Clothes(a, b)
print(c.sum_cloth)

#3
class Cell:
    def __init__(self, mini_cells):
        self.mini_cells=mini_cells
    def __add__(self, other):
        return self.mini_cells + other.mini_cells
    def __sub__(self, other):
        if (self.mini_cells - other.mini_cells) > 0:
            return self.mini_cells - other.mini_cells
        else:
            return "разность количества ячеек двух клеток < нуля!"
    def __mul__(self, other):
        new_cell = self.mini_cells * other.mini_cells
        return new_cell
    def __floordiv__(self, other):
        new_cell = self.mini_cells // other.mini_cells
        return new_cell
    def make_order(self, raw):
        lines = self.mini_cells // raw
        last_line = (self.mini_cells % raw)*'*'
        line = '*'*raw
        print(((line +'\n')*lines) + last_line)
a = Cell(40)
b= Cell(20)
print(a+b, a*b, a-b, a//b)
b.make_order(9)