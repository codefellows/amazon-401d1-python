"""Things to cover...
* What is a module
* What is a script
* How to execute it from CLI
* print/input
* string concatenation
* formatted strings
* if __name__ == "__main__": snippet
"""

VERSION = "0.1"

def input_output():
    print("no console.log for me!")

    print("that's the standard output")

    print("but what about input?")

    color = input("what's my favorite color?")

    color_response = "You're favorite color is " + color + ". Great choice!"

    print(color_response)

    formatted_string = f"You're favorite color is {color}. Great choice!"

    print(formatted_string)

    runnerup_color = input("What's your second favorite color? ")

    faves_template = "Your two favorite colors are {} and {}. Great combo!"

    print(faves_template)

    print(faves_template.format(color, runnerup_color))


def string_methods():
    print("sometimes you have a string with whitespace around it that you want trimmed")

    print("Python has a lot of nice built in methods for stuff like that")

    string_with_white_space = "\n\tspam and eggs\n"

    print(string_with_white_space)

    print(string_with_white_space.strip())


def built_in_modules():
    # https://pymotw.com/3/index.html

    multi_line_string = """
    you can do multiline strings
    by using triple quotation marks
    on both ends which is nice.
    But print this out and there's a problem.
    It's indented.
    Which is great for code formatting.
    But not how we want to display it.
    Never, fear. There's a module for that!
    """

    # this would be at top of file almost always
    from textwrap import dedent

    print(multi_line_string)

    better_multiline_string = dedent(multi_line_string)

    print(better_multiline_string)

    url = "https://pymotw.com/3/index.html"

    print(dedent(f"""Checkout out dedent and more at {url}"""))


def script_vs_module():
    print("hello from a module")


print("I am a module and this print is outside of a function")


if __name__ == "__main__":
    print("I was executed directly as a 'script'")
    print(
        "Try making an 'importer.py' script that imports from me and see what happens"
    )
    print("When you're done here head over to next demo and we'll play a game")

