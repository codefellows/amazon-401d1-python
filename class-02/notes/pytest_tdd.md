# PyTest and Test-Driven Development
Test-driven development is a software development process that relies on the repetition of a very short development cycle: Requirements are turned into very specific test cases, then the software is improved to pass the new tests, only. This is opposed to software development that allows software to be added that is not proven to meet requirements.

TDD is typically approached from a Red, Green, Refactor approach. Red; A test is written which fails because the supporting code to pass the test has not been written yet. Green; The code to pass a previously written test is written to the point which testing succeeds. Refactor; Improvements and further iterations on the code base are made to enhance performance while maintaining the testing standards.

## Basics of Testing
PyTest is a full featured test runner for Python applications. [Full Documentation Here](https://docs.pytest.org/en/latest/contents.html#toc)

Projects created with `Poetry` have PyTest included automatically. Just make sure to install dependencies and activate shell.
```
poetry install
poetry shell
```

An example of a simple test case:
```python
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():  # This is the test definition, pre-fixed function name with `test_`
    assert inc(3) == 5  # This `assert` statement will evaluation whether the conditional is True or False
```

