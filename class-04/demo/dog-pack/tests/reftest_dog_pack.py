from dog_pack import __version__, Puggle, Bulldog


def test_version():
    assert __version__ == "0.1.0"

def test_puggle_name():
    actual = Puggle("Lela").name
    expected = "Lela"
    assert expected == actual


def test_puggle_no_name():
    actual = Puggle().name
    expected = "pooch with no name"
    assert actual == expected


def test_puggle_greet():
    pooch = Puggle("Lela")
    actual = pooch.greet()
    expected = "I am Lela. I am SO HAPPY to meet you!"
    assert actual == expected


def test_puggle_sleep():
    pooch = Puggle("Lela")
    actual = pooch.sleep()
    expected = "zzz"
    assert actual == expected


def test_puggle_name():
    actual = Bulldog("Marv").name
    expected = "Marv"
    assert expected == actual


def test_bulldog_no_name():
    actual = Bulldog().name
    expected = "pooch with no name"
    assert actual == expected


def test_bulldog_greet():
    pooch = Bulldog("Marv")
    actual = pooch.greet()
    expected = "I am Marv. It's a pleasure."
    assert actual == expected


def test_marv_sleep():
    pooch = Bulldog("Marv")
    actual = pooch.sleep()
    expected = "zzz"
    assert actual == expected
