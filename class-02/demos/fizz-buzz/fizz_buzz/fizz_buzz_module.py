def fizz_buzz_func(num):

    result = ""

    if num % 3 == 0:
        result += "Fizz"

    if num % 5 == 0:
        result += "Buzz"

    return result or str(num)

    # if num % 3 == 0 and num % 5 == 0:
    #     return "FizzBuzz"

    # if num % 3 == 0:
    #     return "Fizz"

    # if num % 5 == 0:
    #     return "Buzz"

    # return str(num)
