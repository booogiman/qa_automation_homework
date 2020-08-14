import a as a
import pytest


@pytest.mark.parametrize("params", ["test","test1","test2"])
def test_firstList(params, fixture_str_five):
    test_first_list = ["1","2","3",3,4,5]
    # a = test_first_list.extend(params)
    # type(a)
    # print(a)
    # test_first_list.append(1)
    # print(test_first_list)
    # print(test_first_list,params)
    # print(type(test_first_list),type(params))
    # 11 in test_first_list
    test_first_list.append(params)
    print(fixture_str_five)
    print(test_first_list)
    # print(test_first_list.append(fixture_str_five))

@pytest.mark.parametrize("params", [1,2,3])
def test_secondList(params, fixture_str_five):
    stack = [4,5,6,"green",2.0]
    print(stack)
    stack.append(params*2)
    stack.append(fixture_str_five)
    print(stack)
    assert stack[5] == 6

@pytest.mark.parametrize("params", [1,2,3,4,5,6])
def test_third(params):
    my_new_list=[]
    sum = 0
    my_starting_list = [1,2,3,4,5,6,7,8,9]
    for item in my_starting_list:
        sum += item*params
        my_new_list.append(item*params)
    print(sum)
    assert sum > 135

@pytest.mark.parametrize("params", [[1,2,3,4,5],[1,2,3,4,5],[4,6,7,8,0,9,8,]])
def test_four(four_fixture_list, params):
    a = four_fixture_list.extend(params)
    print(four_fixture_list)
    print(len(four_fixture_list))
    assert len(four_fixture_list)>10

@pytest.mark.parametrize("params", [[1,"2",3,4,5],["1",2,3,4,5,"green"],[4,6,"7",8,0,9,8,"red"],[]])
def test_five(four_fixture_list,params):
    params.extend(four_fixture_list)
    print(params)
    assert params.count(3)>2