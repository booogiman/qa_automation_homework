import pytest
import requests
import argparse
from selenium import webdriver

parser = argparse.ArgumentParser()

parser.add_argument('--brows',
                    help='brows',
                    type=str,
                    default="gh",
                    choices=['gh', 'ff', 'ie']
                    )
# default="gh",
# choices=['gh', 'ff', 'ie']



# def brows_maker(brows):
#     return brows + "//"

args = parser.parse_args()
a = args.brows
# print(a)
# print("test")
@pytest.fixture
def new_browser(request):
    if args.brows == "gh":
        print("gh")
    elif args.brows == "ff":
        print("gh")
    elif args.brows == "ie":
        print("ie")
