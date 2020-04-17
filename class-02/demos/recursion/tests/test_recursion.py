from recursion import __version__
from recursion.factorial import factorial


def test_version():
    assert __version__ == "0.1.0"


def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


def test_factorial_three():
    actual = factorial(3)
    expected = 6
    assert actual == expected


def test_factorial_5():
    actual = factorial(5)
    expected = 120
    assert actual == expected
