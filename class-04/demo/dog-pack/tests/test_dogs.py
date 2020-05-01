import pytest
from dog_pack.dog_pack import Puggle, Boxer, Mutt, Dog


def test_dog_count():
    a = Puggle()
    b = Boxer()
    assert Dog.count == 2


def test_puggle():
    assert Puggle()


def test_puggle_with_name():
    lela = Puggle("Lela")
    actual = lela.name
    expected = "Lela"
    assert actual == expected


def test_puggle_with_unknown_name():
    dunno = Puggle()
    actual = dunno.name
    expected = "unknown"
    assert actual == expected


def test_puggle_greet():
    lela = Puggle("Lela")
    actual = lela.greet()
    expected = "I am SO happy to see you!!!"
    assert actual == expected


def test_puggle_sleep():
    lela = Puggle("Lela")
    actual = lela.sleep()
    expected = "zzz"
    assert actual == expected


def test_boxer():
    assert Boxer()


def test_boxer_with_name():
    marv = Boxer("Marv")
    actual = marv.name
    expected = "Marv"
    assert actual == expected


def test_puggle_with_unknown_name():
    dunno = Boxer()
    actual = dunno.name
    expected = "unknown"
    assert actual == expected


def test_boxer_greet():
    marv = Boxer("Marv")
    actual = marv.greet()
    expected = "Howdy, how's it going?"
    assert actual == expected


def test_boxer_sleep():
    marv = Boxer("Marv")
    actual = marv.sleep()
    expected = "snore"
    assert actual == expected


def test_mutt_greet():
    x = Mutt()
    x.greet()


def test_dog_count():
    Dog.count = 0  # assure known starting point
    a = Puggle()
    b = Boxer()
    assert Dog.count == 2


def test_get_characteristics():
    assert (
        Puggle.get_characteristics() == "Mix of pug and beagle. Looks like a min boxer."
    )
