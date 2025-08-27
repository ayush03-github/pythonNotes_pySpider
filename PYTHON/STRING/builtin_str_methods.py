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
# 2. count()
# Definition: Returns count of substring occurrence
# Use case: Count frequency
# Syntax: string.count(substring, start, end)
# Return type: int
print("banana".count("a"))  # 3

# -----------------------------------------------
# 3. find()
print("hello world".find("world"))  # 6

# 4. index()
print("hello world".index("world"))  # 6

# -----------------------------------------------
# 5. upper()
print("hello".upper())  # HELLO

# 6. lower()
print("HELLO".lower())  # hello

# 7. capitalize()
print("python".capitalize())  # Python

# 8. title()
print("hello world".title())  # Hello World

# 9. swapcase()
print("Hello".swapcase())  # hELLO

# -----------------------------------------------
# 10. isalpha()
print("Hello".isalpha())  # True
print("Hello123".isalpha())  # False

# 11. isdigit()
print("123".isdigit())  # True

# 12. isalnum()
print("abc123".isalnum())  # True

# 13. islower()
print("hello".islower())  # True

# 14. isupper()
print("HELLO".isupper())  # True

# 15. istitle()
print("Hello World".istitle())  # True

# 16. isspace()
print("   ".isspace())  # True

# -----------------------------------------------
# 17. startswith()
print("hello".startswith("he"))  # True

# 18. endswith()
print("hello".endswith("lo"))  # True

# -----------------------------------------------
# 19. strip()
print("  hello  ".strip())  # "hello"

# 20. lstrip()
print("  hello".lstrip())  # "hello"

# 21. rstrip()
print("hello  ".rstrip())  # "hello"

# -----------------------------------------------
# 22. replace()
print("hello world".replace("world", "python"))  # hello python

# 23. split()
print("a,b,c".split(","))  # ['a','b','c']

# 24. rsplit()
print("a,b,c".rsplit(","))  # ['a','b','c']

# 25. splitlines()
print("hello\nworld".splitlines())  # ['hello','world']

# 26. join()
print(",".join(["a","b","c"]))  # a,b,c

# -----------------------------------------------
# 27. zfill()
print("42".zfill(5))  # 00042

# 28. ljust()
print("hi".ljust(5, "-"))  # hi---

# 29. rjust()
print("hi".rjust(5, "-"))  # ---hi

# 30. center()
print("hi".center(6, "*"))  # **hi**

# -----------------------------------------------
# 31. encode()
print("hello".encode())  # b'hello'

# 32. expandtabs()
print("h\te\tl\tl\to".expandtabs(2))  # h e l l o

# -----------------------------------------------
# 33. maketrans() + translate()
trans = str.maketrans("aeiou", "12345")
print("hello world".translate(trans))  # h2ll4 w4rld

# -----------------------------------------------
# 34. format()
print("My name is {}".format("Ayush"))  # My name is Ayush

# 35. format_map()
data = {"x": 10, "y": 20}
print("{x} {y}".format_map(data))  # 10 20

# -----------------------------------------------
# 36. casefold()
print("HELLO".casefold())  # hello (more aggressive lower)

# 37. partition()
print("hello world".partition(" "))  # ('hello',' ','world')

# 38. rpartition()
print("hello world again".rpartition(" "))  # ('hello world',' ','again')

# -----------------------------------------------
# 39. isdecimal()
print("123".isdecimal())  # True

# 40. isnumeric()
print("123".isnumeric())  # True

# 41. isidentifier()
print("var1".isidentifier())  # True

# 42. isprintable()
print("hello".isprintable())  # True

# -----------------------------------------------
# 43. removeprefix() (Python 3.9+)
print("unhappy".removeprefix("un"))  # happy

# 44. removesuffix() (Python 3.9+)
print("automation".removesuffix("tion"))  # automa

# -----------------------------------------------
# 45. __contains__ (via 'in' operator)
print("hello".__contains__("he"))  # True

# 46. __getitem__ (indexing)
print("hello"[1])  # e

# 47. __add__ (concatenation)
print("hi" + " there")  # hi there

# 48. __mul__ (repetition)
print("ha" * 3)  # hahaha
