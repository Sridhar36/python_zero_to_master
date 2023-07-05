import pytest


# def test_login():
#     print("executing login test")
#
#
# def test_user_reg():
#     print("executing user reg test")
#
#
# def test_compose_mail():
#     print("executing compose email test")

# pytest 3_pytest_markers_examples.py -s -v -k   login > only login test
# -k to select a test
#  pytest 3_pytest_markers_examples.py -s -v -k   "not login" > remaining tests

# >> now lets use markers to pick and run test cases <<

@pytest.mark.functional
def test_login():
    print("executing login test")


@pytest.mark.regression
def test_user_reg():
    print("executing user reg test")


@pytest.mark.functional
def test_compose_mail():
    print("executing compose email test")


# pytest 3_pytest_markers_examples.py -s -v -m functional  : will run only tests group with functional
# pytest 3_pytest_markers_examples.py -s -v -m not functional  : will run only tests group with no functional
# we need to register markers in pytest.ini file in below format, then we can avoid warnings in using markers
'''
[pytest]
markers = functional regression
'''


# to skip test
@pytest.mark.skip  # this test will be ignored
def test_to_skip():
    print("skipping test")
