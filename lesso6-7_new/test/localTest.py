import pytest,math

from homework.lesson3.TrigonometricFigures import Triangl,Rectangl,Square,Circle

class TestsTriangl:

    @pytest.mark.parametrize("test_vars", argvalues=[(8,18,12),(15,25,13),(8,9,14)])
    def test_area (self, test_vars):
        side1 = test_vars
        area = Triangl(test_vars)
        p = (test_vars[0] + test_vars[1] + test_vars[2])/2
        test_area = math.sqrt(p*(p-test_vars[0])*(p-test_vars[1])*(p-test_vars[2]))
        if area.area() != test_area:
            print(f"Тестируемое число{area.area()}, сравнивается с расчетным {test_area}. Тест не пройден")
        assert area.area() == test_area
    @pytest.mark.parametrize("test_name_list", ["Триугольник","Прямоугольник","Квадрат","Круг"])
    def test_name (self, test_name_list):
        name = Triangl((8,18,12))
        name.print()
        assert name.nameTrig() == test_name_list

    @pytest.mark.parametrize("test_angels", [0,1,2,3,4,5,6])
    def test_angels(self,test_angels):
        test_triangls = Triangl((8,18,12))
        assert test_triangls.angels() == test_angels

    @pytest.mark.parametrize("test_vars", argvalues=[(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    def test_area(self, test_vars):
        side1 = test_vars
        area = Triangl(test_vars)
        p = test_vars[0] + test_vars[1] + test_vars[2]
        if area.perimetr() != p:
            print(f"Тестируемое число{area.perimetr()}, сравнивается с расчетным {p}. Тест не пройден")
        assert area.perimetr() == p

    # @pytest.mark.parametrize("test_triangl", [(8, 18, 12), (15, 25, 13), (8, 9, 14)])
    # @pytest.mark.parametrize("test_square", [2,3,4,5,6])
    # def test_sum_area(self,test_triangl,test_square):
    #     first_triangl = create_triangl(test_triangl)
    #     first_triangl.print()
    def test_sum_area(self,create_triangl,create_square):
        # create_triangl.area()
        # create_square.area()
        sum = create_triangl.calculatio() + create_square.calculatio()
        print(sum)
        print(create_triangl.add_square(create_square))
        # assert sum == create_square.add_square(create_triangl)

