import math


class TrigFigure:
    def __init__(self, side1):
        self.side1 = side1
        # self.side2 = side2
        # self.side3 = side3

    _corner = None
    _name = ""

    def calculatio(self):
        s = None
        return s

    def area(self):
        print(f"Площадь {self._name}а = {self.calculatio()} ")
        return self.calculatio()

    def nameTrig(self):
        return self._name

    def angels(self):
        print(f"Количество углов в данном {self._name} - {self._corner}")
        return self._corner

    def perimetr(self):
        if self._corner == 0:
            sum = 2 * math.pi * self.side1[0]
        elif self._corner == 3:
            sum = 0
            for i in self.side1:
                sum = sum + i
        elif self._corner == 4 and len(self.side1) == 2:
            sum = (self.side1[0] + self.side1[1]) * 2
        elif self._corner == 4 and len(self.side1) == 1:
            sum = self.side1[0] * 4
        else:
            print("Не верная фигура")
        print(f"Периметр {self._name}а = {sum}")
        return sum

    def print(self):
        self.perimetr()
        self.area()
        self.angels()

    def add_square(self, Figur2):
        # print("тест1")
        # print(issubclass(Figur2, TrigFigure))
        # print(Figur2.set_area()+self.calculatio())
        test_list = (Triangl, Square, Rectangl, Circle)
        # print(Triangl)
        # print(test_list)
        # print(type(test_list))
        # print(Figur2.calculatio())
        if isinstance(Figur2, test_list):
            sum_square = Figur2.calculatio() + self.calculatio()
            test_str = print(f"Сумма площажей фигур: {Figur2._name} и {self._name} = {sum_square}")
        else:
            test_str = print(f"Переданная вами фигура не входит в соства допустимых фигур")
        return test_str,sum_square

# test = TrigFigure(1)
# test.add_square()

class Triangl(TrigFigure):
    def __init__(self, side1):
        super().__init__(side1)

    _corner = 3
    _name = "Триугольник"

    def calculatio(self):
        p = (self.side1[0] + self.side1[1] + self.side1[2]) / 2
        s = math.sqrt(p * (p - self.side1[0]) * (p - self.side1[1]) * (p - self.side1[2]))
        return s


class Rectangl(TrigFigure):
    def __init__(self, side1):
        super().__init__(side1)

    _corner = 4
    _name = "Прямоугольник"

    def calculatio(self):
        s = self.side1[0] * self.side1[1]
        return s
    # def perimetr(self):
    #     perim = (self.side1[0]+self.side1[1]) * 2
    #     print(f"Периметр {self._name}а = {perim}")


class Square(TrigFigure):
    def __init__(self, side1: object) -> object:
        super().__init__(side1)

    _corner = 4
    _name = "Квадрат"

    def calculatio(self):
        s = self.side1[0] * self.side1[0]
        # s = self.side1 * self.side1
        return s


class Circle(TrigFigure):
    def __init__(self, side1):
        super().__init__(side1)

    _corner = 0
    _name = "Круг"

    def calculatio(self):
        s = self.side1[0] * self.side1[0] * math.pi
        return s


class Car:
    pass


circ1 = Circle([3])
circ1.print()
square1 = Square([5])
square1.print()
square1.add_square(circ1)
square1.add_square(Car)
# print(issubclass(circ1, Circle))
# print(isinstance(circ1,Circle))
# print(issubclass(Circle,TrigFigure))
# print(issubclass(circ1,TrigFigure))
# triangl1 = Triangl([3,3,3])
# triangl1.print()
#
# rectangl1 = Rectangl([2,3])
# rectangl1.print()
