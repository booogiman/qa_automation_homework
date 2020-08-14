import pytest


@pytest.mark.parametrize("string_test", ["1111", "2222", "3333"])
def test_one(fixture_str_one, string_test):
    #  print(string_test.isalpha())
    # print(len(string_test))
    # print(string_test.capitalize())
    # print(string_test.upper())
    # print(string_test.upper().isupper())
    assert fixture_str_one == string_test


@pytest.mark.parametrize("string_test", ["1111", "2222", "3333"])
def test_two(fixture_str_one, string_test):
    a = len(string_test)
    b = len(fixture_str_one)
    assert a == b


@pytest.mark.parametrize("string_test", ["fdsavdsvsdaa", "fdsaafdsaJKLcsda", "dsadsadvfdsaav", "321321321321"])
def test_three(fixture_str_second, string_test):
    string_bollen = string_test.isupper()
    string_bollen_fix = fixture_str_second.isupper()
    assert string_bollen == string_bollen_fix


def test_four(first_fixture, fixture_str_one):
    # str1 = fixture_str_one
    print("test")
    print(fixture_str_one.upper())


@pytest.mark.parametrize("string_forward", ["dsa", "Qdsadsa", "gsfds"])
def test_upper(first_fixture, fixture_str_five, string_forward):

    print(string_forward.isalpha(), fixture_str_five.istitle())
    # assert string_forward.isalpha() == fixture_str_five.istitle()
