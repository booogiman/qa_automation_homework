import pytest
import requests


@pytest.mark.parametrize("end_url,expect_num",
                         [("posts", 100), ("comments", 500), ("albums", 100), ("photos", 5000), ("todos", 200),
                          ("users", 10)])
def test_get_all_comment(end_url, expect_num):
    search = requests.get(f"https://jsonplaceholder.typicode.com/{end_url}")
    assert len(search.json()) == expect_num


def test_getcoment():
    search = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    assert isinstance(search.json()[0]["body"], str)


@pytest.mark.parametrize("id", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
def test_getid(id):
    search = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={id}")
    assert search.json()[0]["postId"] == id

def test_getid():
    search = requests.get("https://jsonplaceholder.typicode.com/posts")
    for each in search.json():
        if each["id"] == 2:
            outstring = each["title"]
    assert outstring == "qui est esse"


@pytest.mark.parametrize("id,title_exp", [(91,"repellendus praesentium debitis officiis"), (92,"incidunt et et eligendi assumenda soluta quia recusandae"), (93,"nisi qui dolores perspiciatis")])
def test_userid(id, title_exp):
    search = requests.get("https://jsonplaceholder.typicode.com/albums")
    for each in search.json():
        if each["id"] == id:
            out_title = each["title"]
    assert out_title == title_exp