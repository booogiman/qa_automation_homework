import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--ans",
        default=200,
        help="answer of request"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def answer(request):
    return request.config.getoption("--ans")