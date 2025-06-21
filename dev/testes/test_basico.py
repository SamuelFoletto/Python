def test_soma():
    assert sum([1, 4, 5]) == 10


def is_positive(number):
    return number > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-2) is False