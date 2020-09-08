import requests
import pytest


@pytest.mark.parametrize('number', [1, 2, 3, 4, 5, 7, 8, 9, 10])
def test_first_dog(number):
    response = requests.get(f"https://dog.ceo/api/breed/hound/afghan/images/random/{number}")
    jpg = response.json()
    j = len(jpg['message'])
    print(j)
    assert j == number and jpg['status'] == 'success'


@pytest.mark.parametrize('sub_breeds', ["afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"])

def test_random_sub_breeds(sub_breeds):
    response = requests.get(f'https://dog.ceo/api/breed/hound/{sub_breeds}/images/random')
    j = response.json()['message']
    # print(len(sub_breeds))
    wait_subbreads = j[36:36+len(sub_breeds)]
    assert response.json()['status'] == 'success' and sub_breeds == wait_subbreads


def test_sub_breds():
    response = requests.get("https://dog.ceo/api/breed/terrier/list")
    assert len(response.json()['message']) == 21


def test_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    print(response.json())
    assert response.json()['status'] == "success"

@pytest.mark.parametrize('sub_breed', ['spaniel','hound','mastiff',])
def test_success_subbreeds(sub_breed):
    response_all = requests.get(f"https://dog.ceo/api/breeds/list/all")
    response_spain = requests.get(f'https://dog.ceo/api/breed/{sub_breed}/list')
    print(response_all.json()['message'][sub_breed])
    print(response_spain.json()['message'])
    assert response_all.json()['message'][sub_breed] == response_spain.json()['message']


