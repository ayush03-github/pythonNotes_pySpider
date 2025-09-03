# String Built-in Methods in Python

# -----------------------------------------------
# 1. len()
# Definition: Returns number of characters in a string
# Use case: To check length of string
# Syntax: len(string)
# Return type: int
text = "Hello"
print(len(text))  # 5

# -----------------------------------------------
# 2. capitalize()
# Definition: Converts the first character of a string to uppercase
# Use case: To format sentences with proper capitalization
# Syntax: string.capitalize()
# Return type: str
text = "hello world"
print(text.capitalize())  # Hello world

# -----------------------------------------------
# 3. casefold()
# Definition: Converts string into lowercase (more aggressive than lower)
# Use case: Case-insensitive comparisons
# Syntax: string.casefold()
# Return type: str
text = "HELLOß"
print(text.casefold())  # helloß → helloss

# -----------------------------------------------
# 4. center()
# Definition: Returns a centered string of specified width
# Use case: For formatting outputs
# Syntax: string.center(width, fillchar)
# Return type: str
text = "Hello"
print(text.center(10, "-"))  # --Hello---

# -----------------------------------------------
# 5. count()
# Definition: Returns the number of occurrences of a substring
# Use case: To find frequency of substring
# Syntax: string.count(substring, start, end)
# Return type: int
text = "banana"
print(text.count("a"))  # 3

# -----------------------------------------------
# 6. encode()
# Definition: Encodes the string into bytes
# Use case: Converting text into byte representation
# Syntax: string.encode(encoding, errors)
# Return type: bytes
text = "Hello"
print(text.encode())  # b'Hello'

# -----------------------------------------------
# 7. endswith()
# Definition: Checks if string ends with specified suffix
# Use case: File extension checks
# Syntax: string.endswith(suffix, start, end)
# Return type: bool
text = "hello.txt"
print(text.endswith(".txt"))  # True

# -----------------------------------------------
# 8. expandtabs()
# Definition: Replaces tabs with spaces
# Use case: Aligning text properly
# Syntax: string.expandtabs(tabsize)
# Return type: str
text = "H\te\tl\tl\to"
print(text.expandtabs(2))  # H e l l o

# -----------------------------------------------
# 9. find()
# Definition: Returns the first index of substring or -1 if not found
# Use case: Locate substring in string
# Syntax: string.find(substring, start, end)
# Return type: int
text = "hello world"
print(text.find("world"))  # 6

# -----------------------------------------------
# 10. format()
# Definition: Formats string with placeholders
# Use case: Dynamic string formatting
# Syntax: string.format(values)
# Return type: str
text = "My name is {}".format("Ayush")
print(text)  # My name is Ayush

# -----------------------------------------------
# 11. format_map()
# Definition: Formats string using dictionary mapping
# Use case: Dynamic templates
# Syntax: string.format_map(mapping)
# Return type: str
data = {"name": "Ayush", "age": 21}
text = "My name is {name}, I am {age}".format_map(data)
print(text)  # My name is Ayush, I am 21

# -----------------------------------------------
# 12. index()
# Definition: Returns the first index of substring (error if not found)
# Use case: Safer find when substring must exist
# Syntax: string.index(substring, start, end)
# Return type: int
text = "hello world"
print(text.index("world"))  # 6

# -----------------------------------------------
# 13. isalnum()
# Definition: Checks if all characters are alphanumeric
# Use case: Validation for identifiers
# Syntax: string.isalnum()
# Return type: bool
text = "Hello123"
print(text.isalnum())  # True

# -----------------------------------------------
# 14. isalpha()
# Definition: Checks if all characters are alphabets
# Use case: Validate alphabetic input
# Syntax: string.isalpha()
# Return type: bool
text = "Hello"
print(text.isalpha())  # True

# -----------------------------------------------
# 15. isascii()
# Definition: Checks if all characters are ASCII
# Use case: Ensure data is ASCII only
# Syntax: string.isascii()
# Return type: bool
text = "Hello"
print(text.isascii())  # True

# -----------------------------------------------
# 16. isdecimal()
# Definition: Checks if all characters are decimals
# Use case: Validate numeric input
# Syntax: string.isdecimal()
# Return type: bool
text = "1234"
print(text.isdecimal())  # True

# -----------------------------------------------
# 17. isdigit()
# Definition: Checks if all characters are digits
# Use case: Identify numbers
# Syntax: string.isdigit()
# Return type: bool
text = "123"
print(text.isdigit())  # True

# -----------------------------------------------
# 18. isidentifier()
# Definition: Checks if string is a valid Python identifier
# Use case: Validation of variable names
# Syntax: string.isidentifier()
# Return type: bool
text = "my_var"
print(text.isidentifier())  # True

# -----------------------------------------------
# 19. islower()
# Definition: Checks if all characters are lowercase
# Use case: Case validation
# Syntax: string.islower()
# Return type: bool
text = "hello"
print(text.islower())  # True

# -----------------------------------------------
# 20. isnumeric()
# Definition: Checks if all characters are numeric
# Use case: Validate numeric input including fractions, superscripts
# Syntax: string.isnumeric()
# Return type: bool
text = "123"
print(text.isnumeric())  # True

# -----------------------------------------------
# 21. isprintable()
# Definition: Checks if all characters are printable
# Use case: Validation for displayable text
# Syntax: string.isprintable()
# Return type: bool
text = "Hello"
print(text.isprintable())  # True

# -----------------------------------------------
# 22. isspace()
# Definition: Checks if all characters are whitespace
# Use case: Detect blank inputs
# Syntax: string.isspace()
# Return type: bool
text = "   "
print(text.isspace())  # True

# -----------------------------------------------
# 23. istitle()
# Definition: Checks if string is in title case
# Use case: Title formatting validation
# Syntax: string.istitle()
# Return type: bool
text = "Hello World"
print(text.istitle())  # True

# -----------------------------------------------
# 24. isupper()
# Definition: Checks if all characters are uppercase
# Use case: Case validation
# Syntax: string.isupper()
# Return type: bool
text = "HELLO"
print(text.isupper())  # True

# -----------------------------------------------
# 25. join()
# Definition: Joins iterable elements with string as separator
# Use case: Convert list to string
# Syntax: separator.join(iterable)
# Return type: str
words = ["Hello", "World"]
print(" ".join(words))  # Hello World

# -----------------------------------------------
# 26. ljust()
# Definition: Returns a left-justified string
# Use case: Formatting
# Syntax: string.ljust(width, fillchar)
# Return type: str
text = "Hello"
print(text.ljust(10, "-"))  # Hello-----

# -----------------------------------------------
# 27. lower()
# Definition: Converts string to lowercase
# Use case: Case normalization
# Syntax: string.lower()
# Return type: str
text = "HELLO"
print(text.lower())  # hello

# -----------------------------------------------
# 28. lstrip()
# Definition: Removes leading whitespace or specified chars
# Use case: Clean text input
# Syntax: string.lstrip(chars)
# Return type: str
text = "   Hello"
print(text.lstrip())  # Hello

# -----------------------------------------------
# 29. maketrans()
# Definition: Returns a mapping table for translations
# Use case: Used with translate() for character replacements
# Syntax: str.maketrans(x, y, z)
# Return type: dict
table = str.maketrans("H", "J")
print("Hello".translate(table))  # Jello

# -----------------------------------------------
# 30. partition()
# Definition: Splits string into 3 parts (before, match, after)
# Use case: Splitting once
# Syntax: string.partition(separator)
# Return type: tuple
text = "hello world"
print(text.partition(" "))  # ('hello', ' ', 'world')

# -----------------------------------------------
# 31. removeprefix()
# Definition: Removes prefix if present
# Use case: Clean known prefixes
# Syntax: string.removeprefix(prefix)
# Return type: str
text = "unhappy"
print(text.removeprefix("un"))  # happy

# -----------------------------------------------
# 32. removesuffix()
# Definition: Removes suffix if present
# Use case: Clean known suffixes
# Syntax: string.removesuffix(suffix)
# Return type: str
text = "reading.txt"
print(text.removesuffix(".txt"))  # reading

# -----------------------------------------------
# 33. replace()
# Definition: Replaces occurrences of substring
# Use case: Find & replace
# Syntax: string.replace(old, new, count)
# Return type: str
text = "Hello World"
print(text.replace("World", "Python"))  # Hello Python

# -----------------------------------------------
# 34. rfind()
# Definition: Returns highest index of substring or -1
# Use case: Find last occurrence
# Syntax: string.rfind(substring, start, end)
# Return type: int
text = "banana"
print(text.rfind("a"))  # 5

# -----------------------------------------------
# 35. rindex()
# Definition: Returns highest index of substring (error if not found)
# Use case: Find last occurrence (strict)
# Syntax: string.rindex(substring, start, end)
# Return type: int
text = "banana"
print(text.rindex("a"))  # 5

# -----------------------------------------------
# 36. rjust()
# Definition: Returns right-justified string
# Use case: Formatting
# Syntax: string.rjust(width, fillchar)
# Return type: str
text = "Hello"
print(text.rjust(10, "-"))  # -----Hello

# -----------------------------------------------
# 37. rpartition()
# Definition: Splits into 3 parts at last occurrence
# Use case: Split once from right
# Syntax: string.rpartition(separator)
# Return type: tuple
text = "hello world"
print(text.rpartition(" "))  # ('hello', ' ', 'world')

# -----------------------------------------------
# 38. rsplit()
# Definition: Splits string from right
# Use case: Control split direction
# Syntax: string.rsplit(separator, maxsplit)
# Return type: list
text = "a,b,c"
print(text.rsplit(",", 1))  # ['a,b', 'c']

# -----------------------------------------------
# 39. rstrip()
# Definition: Removes trailing whitespace or chars
# Use case: Clean text
# Syntax: string.rstrip(chars)
# Return type: str
text = "Hello   "
print(text.rstrip())  # Hello

# -----------------------------------------------
# 40. split()
# Definition: Splits string into list
# Use case: Tokenization
# Syntax: string.split(separator, maxsplit)
# Return type: list
text = "a b c"
print(text.split())  # ['a', 'b', 'c']

# -----------------------------------------------
# 41. splitlines()
# Definition: Splits string at line breaks
# Use case: Reading multiline text
# Syntax: string.splitlines(keepends)
# Return type: list
text = "Hello\nWorld"
print(text.splitlines())  # ['Hello', 'World']

# -----------------------------------------------
# 42. startswith()
# Definition: Checks if string starts with prefix
# Use case: File path validation
# Syntax: string.startswith(prefix, start, end)
# Return type: bool
text = "hello world"
print(text.startswith("hello"))  # True

# -----------------------------------------------
# 43. strip()
# Definition: Removes leading and trailing whitespace/chars
# Use case: Clean input
# Syntax: string.strip(chars)
# Return type: str
text = "   Hello   "
print(text.strip())  # Hello

# -----------------------------------------------
# 44. swapcase()
# Definition: Swaps lowercase to uppercase and vice versa
# Use case: Toggle case
# Syntax: string.swapcase()
# Return type: str
text = "Hello World"
print(text.swapcase())  # hELLO wORLD

# -----------------------------------------------
# 45. title()
# Definition: Converts string to title case
# Use case: Proper case formatting
# Syntax: string.title()
# Return type: str
text = "hello world"
print(text.title())  # Hello World

# -----------------------------------------------
# 46. translate()
# Definition: Replaces characters based on mapping
# Use case: Custom character replacement
# Syntax: string.translate(mapping)
# Return type: str
table = str.maketrans("H", "J")
print("Hello".translate(table))  # Jello

# -----------------------------------------------
# 47. upper()
# Definition: Converts string to uppercase
# Use case: Case normalization
# Syntax: string.upper()
# Return type: str
text = "hello"
print(text.upper())  # HELLO

# -----------------------------------------------
# 48. zfill()
# Definition: Pads string with zeros on the left
# Use case: Formatting numbers
# Syntax: string.zfill(width)
# Return type: str
text = "42"
print(text.zfill(5))  # 00042
