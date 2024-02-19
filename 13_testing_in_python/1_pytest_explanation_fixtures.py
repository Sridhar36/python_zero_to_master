import pytest


def test_login():
    print("executing login test")


# Any pytest file should  start with test_ or it should end with _test
# Pytest method names should start with test

# to change run configuration in Python using Pycharm
# click on edit configuration
# click on ' + ' icon
# python tests > select pytests > select the script in target column
# apply and save

# to execute a specific file: pytest test_login.py -s -v
# -s prints print statements to console
# -v verbose added.

def test_user_registration():
    print("executing registration")


# >>>     Defining test fixtures        <<<<<<<<
# if you want to do a piece of code everywhere before every test case gets executed
# For this we can create test fixtures..
# we can define fixtures for function level or module level

# function fixture configured at function level.
# mandatory it has to be same naming convention for these fixtures below..
def setup_function(function):
    print("launching browser at function level")


# teardown func - executes after each test method..
def teardown_function(function):
    print("quitting browser")


# FOR MODULE LEVEL
def setup_module(module):
    print("Setup DB connection")


def teardown_module(module):
    print("closing DB connection")
