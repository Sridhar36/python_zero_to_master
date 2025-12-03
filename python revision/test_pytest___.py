import pytest

@pytest.mark.parametrize("number", [1, 2, 3])
def test_is_positive(number):
    assert number > 0





@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-1, 1, 0),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected





@pytest.mark.parametrize(
    "username, status_code",
    [
        ("valid_user", 200),
        ("invalid_user", 404),
    ],
    ids=["valid user login", "invalid user login"]
)
def test_get_user(username, status_code):
    assert True  # dummy


@pytest.mark.parametrize(
    "username, status_code",
    [
        ("valid_user", 200),
        ("invalid_user", 404),
    ],
    ids=["valid user login", "invalid user login"]
)
def test_get_user(username, status_code):
    assert True  # dummy

