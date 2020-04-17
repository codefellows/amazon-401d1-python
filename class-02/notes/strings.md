# Fun with Python Strings

## String formatting
The `str.format()` method and the `Formatter` class share the same syntax for format strings (although in the case of `Formatter`, subclasses can define their own format string syntax).

Format strings contain “replacement fields” surrounded by curly braces {}. Anything that is not contained in braces is considered literal text, which is copied unchanged to the output. If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.

Some simple format string examples:
```python
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
```
For more in depth detail about string formatting, see [String Formatting Docs](https://docs.python.org/2/library/string.html#format-string-syntax)

## Parsing strings
Parsing strings using the built-in methods and properties is fairly consistent between languages. Python's implementations follow a standard line of thought in how string objects are broken apart and/or reconstructed.

Some of the simplest methods include `.split()` and `.join()` though their actual usage may differ slightly from other languages.
```python
str = 'The quick brown fox.'
words = str.split(' ')
words
# ['The', 'quick', 'brown', 'fox.']
new_str = '-'.join(words)
new_str
# 'The-quick-brown-fox.'
```
Strings can also be accessed as an iterable, using the sub-syntax (square brackets).
```python
str = 'The quick brown fox.'
str[0:8]  # Qualifies the 1st to the 9th characters in the str using 0-indexing
# 'The quic'
str[8:-1]
# 'k brown fo'
```

### Datetime
`datetime` objects can also be used to format strings.
```python
import datetime
'{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
# '2014-02-07 11:52:21'
```
