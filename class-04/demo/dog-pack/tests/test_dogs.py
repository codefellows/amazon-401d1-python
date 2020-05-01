import pytest
from dog_pack import Puggle, Boxer


def test_puggle():
    assert Puggle()


def test_puggle_no_name():
    pooch = Puggle()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_puggle_name():
    puggle = Puggle("Marv")
    actual = puggle.name
    expected = "Marv"
    assert actual == expected


def test_puggle_greet(marv):
    actual = marv.greet()
    expected = "I am Marv. I am SO HAPPY to meet you!"
    assert actual == expected


def test_puggle_sleep(marv):
    actual = marv.sleep()
    expected = "zzz"
    assert actual == expected


def test_boxer():
    assert Boxer()


def test_boxer_no_name():
    pooch = Boxer()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_boxer_name(lela):
    actual = lela.name
    expected = "Lela"
    assert actual == expected


def test_boxer_greet(lela):
    actual = lela.greet()
    expected = "The name's Lela. Pleasure."
    assert actual == expected


def test_boxer_sleep(marv):
    actual = marv.sleep()
    expected = "zzz"
    assert actual == expected


def test_puggle_class_characteristics():
    actual = Puggle.get_characteristics()
    expected = "Like a mini boxer"
    assert actual == expected


def test_puggle_count():
    actual = Puggle.get_breed_count()
    expected = 0
    assert actual == expected

    Puggle("Marv")

    actual = Puggle.get_breed_count()
    expected = 1
    assert actual == expected


@pytest.fixture(autouse=True)
def prep():
    """Reset the Puggle count so it's fresh each test run
    """
    Puggle.count = 0


@pytest.fixture
def marv():
    return Puggle("Marv")


@pytest.fixture
def lela():
    return Boxer("Lela")

