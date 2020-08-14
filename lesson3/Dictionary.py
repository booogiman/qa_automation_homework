import pytest


@pytest.mark.parametrize("test_dict",
                         [{'color': 'red', 'num': 1}, {'color': 'green', 'num': 2}, {'color': 'blue', 'num': 3},
                          {'color': 'black', 'num': 4}])
def test_first_dict(test_dict, fixture_str_one):
    print(test_dict, fixture_str_one)

    print(test_dict["color"] == fixture_str_one)


@pytest.mark.parametrize("test_dic",
                         [{'color': 'red', 'num': 1}, {'color': 'green', 'num': 2}, {'color': 'blue', 'num': 3},
                          {'color': 'black', 'num': 4}])
def test_second_dict(test_dic, five_fixture_set):
    print(f"{test_dic} = {five_fixture_set}")
    print(test_dic == five_fixture_set)


@pytest.mark.parametrize("test_value", [["red", "green", "blue", "white"], "blackkk"])
def test_third_dict(fixture_str_five, test_value):
    test_key = fixture_str_five
    print(dict(zip(test_key, test_value)))


@pytest.mark.parametrize("test_value", [["red", "green", "blue", "white"], "black"])
def test_four_dick(fixture_str_five, test_value):
    test_dic = {'color': 'red', 'num': 1}
    test_key = fixture_str_five
    test_dic[test_key] = test_value
    print(test_dic)


@pytest.mark.parametrize("test_dic",
                         [{'color': 'red', 'num': 1}, {'color': 'green', 'num': 2}, {'color': 'blue', 'num': 3},
                          {'color': 'black', 'num': 4}])
def test_five_dick(test_dic, six_fixture_set):
    if six_fixture_set in test_dic:
        print(f"{six_fixture_set} - Да такой ключ есть!")
    else:
        print(f"{six_fixture_set} - Этот ключ отсутствует в словаре")
