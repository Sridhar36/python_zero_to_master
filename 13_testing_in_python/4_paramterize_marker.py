import pytest


def get_data():
    return [
        ("abc", "123"), ("bcd", "456"), ("xcv", "099")
    ]


@pytest.mark.parametrize("username", "password", get_data())
def test_dologin(username, password):
    print(username, "--", password)
