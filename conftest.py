# import pytest
#
# from homework.lesson3.TrigonometricFigures import Triangl,Rectangl,Square,Circle
#
# @pytest.fixture
# def fixtyre_new_triangl():
#
#     return [(8, 18, 12), (15, 25, 13), (8, 9, 14)]
# @pytest.fixture(params=[(8, 18, 12), (15, 25, 13), (8, 9, 14)])
# def create_triangl(request):
#     return Triangl(request.param)
#
# @pytest.fixture(params=[(1,2),(2,3),(3,4)])
# def create_square(request):
#     return Square(request.param)