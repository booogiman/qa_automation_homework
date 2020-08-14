import pytest

@pytest.mark.parametrize("params",[6,7,8,9,1,2,3,654,34,543,432432,5643])
def test_first_set(params,first_fixture_list):
    test_set = {1,2,3,45,6,7,78}

    test_set.add(params)
    test_set.add(first_fixture_list)
    print(test_set)
    # print(len(test_set))
    assert len(test_set)>7

@pytest.mark.parametrize("params",[{6,7,8},{6,6,6,6},{7,7,7,74,3,25},{1,2,3,45,6,7,8},{665,786,"dsa",54,45,2,1,5,5,5,5,5},{1,"sd",3,4,5,6,7}])
def test_second_set(params,four_fixture_set):
    test_set = {1, 2, 3, 45, 6, 7, 78}
    # four_fixture_list.append(test_set)
    # print(four_fixture_list)
    a = test_set.difference(params,four_fixture_set)
    print(a)
    assert len(a) == 2

@pytest.mark.parametrize("params",[{6,7,8},{6,6,6,6},{7,7,7,74,3,25},{1,2,3,45,6,7,8},{665,786,"dsa",54,45,2,1,5,5,5,5,5},{1,"sd",3,4,5,6,7}])
def test_third_set(params):
    test_set = {11,11, 2, 3, 45, 6, 7, 78,3,3,33,3,3,3,33,3,3,31,1,1,1,11}
    a = params.issubset(test_set)
    assert a

@pytest.mark.parametrize("param",[{6,7,8},{6,6,6,6},{7,7,7,74,3,25},{1,2,3,45,6,7,8},{665,786,"dsa",54,45,2,1,5,5,5,5,5},{1,"sd",3,4,5,6,7}])
def test_four_set(param,four_fixture_set):
    # print(param.union(four_fixture_set))
    assert len(param.union((four_fixture_set))) < 8

@pytest.mark.parametrize("param",[{6,7,8},{6,6,6,6},{7,7,7,74,3,25},{1,2,3,45,6,7,8},{665,786,"dsa",54,45,2,1,5,5,5,5,5},{1,"sd",3,4,5,6,7}])
def test_five_set(param,four_fixture_set):
    print(param)
    print(four_fixture_set)
    assert param.isdisjoint(four_fixture_set)
