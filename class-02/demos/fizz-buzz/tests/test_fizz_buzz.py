from fizz_buzz.fizz_buzz_module import fizz_buzz_func


def test_fizz_buzz_1():
    assert fizz_buzz_func(1) == "1"


def test_fizz_buzz_2():
    assert fizz_buzz_func(2) == "2"


def test_fizz_buzz_3():
    assert fizz_buzz_func(3) == "Fizz"


def test_fizz_buzz_4():
    assert fizz_buzz_func(4) == "4"


def test_fizz_buzz_5():
    assert fizz_buzz_func(5) == "Buzz"


def test_fizz_buzz_6():
    assert fizz_buzz_func(6) == "Fizz"


def test_fizz_buzz_10():
    assert fizz_buzz_func(10) == "Buzz"


def test_fizz_buzz_15():
    assert fizz_buzz_func(15) == "FizzBuzz"


def test_fizz_buzz_30():
    assert fizz_buzz_func(30) == "FizzBuzz"
