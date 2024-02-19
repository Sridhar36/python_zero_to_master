# test case name in Python is method names
# we write each script as a test method

def test_firstprogram():
    msg = "Hello"


def test_credit_card_name():
    print("credit card name")


def test_credit_card_partner():
    print("regular expression..")


# to run test scripts that are related only to credit cards we can use
# py.test -k credit_card -v -s
# -k stands for method names eecution
# -s logs in out put
# -v stands for more info metadata
# you can run specific file with py.test <filename>

'''Grouping tests with pytest marks'''
# consider a scenario we want to run smoke, sanity or regression, we can use marks
# in cucumber we use tags and in pytest we use marks

import pytest


@pytest.mark.smoke
def test_first():
    print("credit card name")


@pytest.mark.smoke
def test_second():
    print("regular expression..")

# use keyword m in pytest command to run test cases that marks
# py.test -m smoke -v -s