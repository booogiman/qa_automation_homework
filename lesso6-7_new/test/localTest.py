import pytest, math

from homework.les6.TrigonometricFigures import Triangl, Rectangl, Square, Circle


class TestsTriangl1:

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    def test_area(self, test_vars):
        side1 = test_vars
        area = Triangl(test_vars)
        p = (test_vars[0] + test_vars[1] + test_vars[2]) / 2
        test_area = math.sqrt(p * (p - test_vars[0]) * (p - test_vars[1]) * (p - test_vars[2]))
        if area.area() != test_area:
            print(f"Тестируемое число{area.area()}, сравнивается с расчетным {test_area}. Тест не пройден")
        assert area.area() == test_area

    @pytest.mark.parametrize("test_name_list", ["Триугольник", "Прямоугольник", "Квадрат", "Круг"])
    def test_name(self, test_name_list):
        name = Triangl((8, 18, 12))
        name.print()
        assert name.nameTrig() == test_name_list

    @pytest.mark.parametrize("test_angels", [0, 1, 2, 3, 4, 5, 6])
    def test_angels(self, test_angels):
        test_triangls = Triangl((8, 18, 12))
        assert test_triangls.angels() == test_angels

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    def test_perimetr(self, test_vars):
        side1 = test_vars
        area = Triangl(test_vars)
        p = test_vars[0] + test_vars[1] + test_vars[2]
        if area.perimetr() != p:
            print(f"Тестируемое число{area.perimetr()}, сравнивается с расчетным {p}. Тест не пройден")
        assert area.perimetr() == p

    @pytest.mark.parametrize("test_triangl", [(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    @pytest.mark.parametrize("test_rect", [(1,2), (4,4), (9,7), (10,15), (9,9)])
    def test_sum_area(self, test_triangl, test_rect):
        triangl = Triangl(test_triangl)
        rect = Rectangl(test_rect)
        sum = triangl.calculatio() + rect.calculatio()
        assert sum == triangl.add_square(rect)

class TestsRectangl1:

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18), (15, 25), (8, 9)])
    def test_area(self, test_vars):
        side1 = test_vars
        area = Rectangl(test_vars)
        test_area = test_vars[0]*test_vars[1]
        if area.area() != test_area:
            print(f"Тестируемое число{area.area()}, сравнивается с расчетным {test_area}. Тест не пройден")
        assert area.area() == test_area

    @pytest.mark.parametrize("test_name_list", ["Триугольник", "Прямоугольник", "Квадрат", "Круг"])
    def test_name(self, test_name_list):
        name = Rectangl((8, 18))
        name.print()
        assert name.nameTrig() == test_name_list

    @pytest.mark.parametrize("test_angels", [0, 1, 2, 3, 4, 5, 6])
    def test_angels(self, test_angels):
        test_rect = Rectangl((8, 18))
        assert test_rect.angels() == test_angels

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18), (15, 25), (8, 9)])
    def test_perimetr(self, test_vars):
        side1 =Rectangl(test_vars)
        p = (test_vars[0] + test_vars[1])*2
        if side1.perimetr() != p:
            print(f"Тестируемое число{side1.perimetr()}, сравнивается с расчетным {p}. Тест не пройден")
        assert side1.perimetr() == p

    @pytest.mark.parametrize("test_triangl", [(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    @pytest.mark.parametrize("test_rect", [(1,2), (4,4), (9,7), (10,15), (9,9)])
    def test_sum_area(self, test_triangl, test_rect):
        triangl = Triangl(test_triangl)
        rect = Rectangl(test_rect)
        sum = rect.calculatio() + triangl.calculatio()
        assert sum == rect.add_square(triangl)

class TestsSquare1:

    @pytest.mark.parametrize("test_vars", argvalues=[18, 17, 32])
    def test_area(self, test_vars):
        area = Square(test_vars)
        test_area = test_vars*test_vars
        if area.area() != test_area:
            print(f"Тестируемое число{area.area()}, сравнивается с расчетным {test_area}. Тест не пройден")
        assert area.area() == test_area

    @pytest.mark.parametrize("test_name_list", ["Триугольник", "Прямоугольник", "Квадрат", "Круг"])
    def test_name(self, test_name_list):
        name = Square(20)
        name.print()
        assert name.nameTrig() == test_name_list

    @pytest.mark.parametrize("test_angels", [0, 1, 2, 3, 4, 5, 6])
    def test_angels(self, test_angels):
        test_rect = Square(12)
        assert test_rect.angels() == test_angels

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18), (15, 25), (8, 9)])
    def test_perimetr(self, test_vars):
        side1 =Rectangl(test_vars)
        p = (test_vars[0] + test_vars[1])*2
        if side1.perimetr() != p:
            print(f"Тестируемое число{side1.perimetr()}, сравнивается с расчетным {p}. Тест не пройден")
        assert side1.perimetr() == p

    @pytest.mark.parametrize("test_triangl", [(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    @pytest.mark.parametrize("test_square", [20, 35, 17, 22, 34])
    def test_sum_area(self, test_triangl, test_square):
        triangl = Triangl(test_triangl)
        square = Square(test_square)
        sum = square.calculatio() + triangl.calculatio()
        assert sum == square.add_square(triangl)


class TestsCircl1:

    @pytest.mark.parametrize("test_vars", argvalues=[8, 15, 8])
    def test_area(self, test_vars):
        area = Circle(test_vars)
        test_area = test_vars*test_vars*math.pi
        if area.area() != test_area:
            print(f"Тестируемое число{area.area()}, сравнивается с расчетным {test_area}. Тест не пройден")
        print(area.nameTrig())
        assert area.area() == test_area

    @pytest.mark.parametrize("test_name_list", ["Триугольник", "Прямоугольник", "Квадрат", "Круг"])
    def test_name(self, test_name_list):
        name = Circle(8)
        assert name.nameTrig() == test_name_list

    @pytest.mark.parametrize("test_angels", [0, 1, 2, 3, 4, 5, 6])
    def test_angels(self, test_angels):
        test_rect = Circle(8)
        assert test_rect.angels() == test_angels

    @pytest.mark.parametrize("test_vars", argvalues=[8, 25, 10])
    def test_perimetr(self, test_vars):
        side1 =Circle(test_vars)
        p = 2 * math.pi * test_vars
        if side1.perimetr() != p:
            print(f"Тестируемое число{side1.perimetr()}, сравнивается с расчетным {p}. Тест не пройден")
        assert side1.perimetr() == p

    @pytest.mark.parametrize("test_circl", [3, 5, 6, 7, 9, 2])
    @pytest.mark.parametrize("test_rect", [(1,2), (4,4), (9,7), (10,15), (9,9)])
    def test_sum_area(self, test_circl, test_rect):
        circl = Circle(test_circl)
        rect = Rectangl(test_rect)
        sum = rect.calculatio() + circl.calculatio()
        assert sum == circl.add_square(rect)