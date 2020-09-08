import pytest
import requests


def test_all_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_state=new_york")
    data = response.json()
    for each in data:
        if each["state"] == "New York":
            answer = 1
        else: answer = 0
    assert answer == 1


@pytest.mark.parametrize("_id", [1, 2, 3, 32, 432, 444, 123])
def test_get_brewer_by_id(_id):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/{_id}")
    assert _id == response.json()["id"]


@pytest.mark.parametrize("type, expect_numbers",
                         [("micro", 20), ("regional", 20), ("brewpub", 20), ("large", 20), ("planning", 20), ("bar", 1),
                          ("contract", 20), ("proprietor", 20)])
def test_number_off_typeBrewery(type, expect_numbers):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={type}")
    assert len(response.json()) == expect_numbers


def test_pages():
    response = requests.get(f"https://api.openbrewerydb.org/breweries?page=1")
    assert response.json()[0]["id"] == 2


@pytest.mark.parametrize("num_on_page", [4, 6, 12, 50, 23, 6, 34])
def test_num_brewery_on_page(num_on_page):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?per_page={num_on_page}")
    assert len(response.json()) == num_on_page
