import pytest


# >>>>>>>>>>> using decorators with test fixtures <<<<<<

@pytest.fixture(scope='module')  # this is decorator
def setup():
    print("creating DB connection")
    yield
    print("closing DB connection")


@pytest.fixture(scope='function')
def before():
    print("launching browser")
    yield
    print("closing browser")


# def test_login(setup, before):  # this is one way to give fixtures
#     print("Executing login")

# this is another way to use fixtures using use fixtures mark

@pytest.mark.usefixtures("setup", "before")
def test_login(setup, before):
    print("Executing login")
