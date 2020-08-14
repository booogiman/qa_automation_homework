import pytest


@pytest.fixture(params=["first", "second", "1111", "2222"])
def fixture_str_one(request):
    return request.param


@pytest.fixture(params=["HUKHU", "sesdUIUIcond", "1111", "2222", ""])
def fixture_str_second(request):
    return request.param


@pytest.fixture(params=[21, 22, 23, 24, 25])
def fixture_str_second2(request):
    return request.param


@pytest.fixture(params=["Adsadsa", "cdsadsa", "Bdsdsa", "ndsadsa", "Fggggfdsaf"])
def fixture_str_five(request):
    return request.param


@pytest.fixture
def first_fixture():
    print("Start test")


@pytest.fixture(params=[1, 2, 3, 4, 5, 677, 8, 9])
def first_fixture_list(request):
    print(request.param)
    a = request.param * 2
    print(a)
    return a


@pytest.fixture(
    params=[[1, 2, 3, 4, 5], [5666, 6, 6, 6, 6, ], [9, 2, 3, 44, 5, 6, 7, 2, 5, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3]])
def four_fixture_list(request):
    return request.param


@pytest.fixture(
    params=[{1, 2, 3, 4, 5}, {5666, 6, 6, 6, 6, }, {9, 2, 3, 44, 5, 6, 7, 2, 5, 4}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3},
            {23, 1, 2, 3, 4, 543, 435, 6, 2}])
def four_fixture_set(request):
    return request.param


@pytest.fixture(params=[{'color': 'blue', 'num': 1}, {'color': 'green', 'num': 2}, {'color': 'blue', 'num': 3},
                        {'color': 'black', 'num': 4}])
def five_fixture_set(request):
    return request.param


@pytest.fixture(params=["black", "blue", "red", 1, 2, 3, 4, "cat", "color"])
def six_fixture_set(request):
    return request.param
