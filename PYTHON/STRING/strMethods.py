# initialize a string 

str = "ayush kodle"
print(str)

# now there are "" total methods in python

#1. .len() --> int : is used to return the total length of string

print(len(str))

#  OP : 11

# 2. .count(substring) --> int : is to get the number of times a sustring is appeared

count = str.count('a')
print(count)

# 3. .startswith(prefix) --> boolean : is used to check where the pass string is prefix of the string or not

print(str.startswith("ayu"))

# 4. .endswith(suffix) --> boolean : is used to check whether the passed string is a suffix or not

print(str.endswith("le"))

# B. Case Conversion Methods
# 5. .upper() --> str : converts all letters to uppercase
print(str.upper())  
# OP : AYUSH KODLE

# 6. .lower() --> str : converts all letters to lowercase
print(str.lower())  
# OP : ayush kodle

# 7. .title() --> str : capitalizes first letter of each word
print(str.title())  
# OP : Ayush Kodle

# 8. .capitalize() --> str : capitalizes first letter of the string
print(str.capitalize())  
# OP : Ayush kodle

# 9. .swapcase() --> str : swaps lowercase to uppercase and vice versa
print(str.swapcase())  
# OP : AYUSH KODLE


# C. Searching / Indexing Methods
# 10. .find(substring) --> int : returns index of substring (or -1 if not found)
print(str.find("kod"))  
# OP : 6

# 11. .rfind(substring) --> int : returns last index of substring (or -1 if not found)
print(str.rfind("o"))  
# OP : 7

# 12. .index(substring) --> int : returns index of substring (error if not found)
print(str.index("kod"))  
# OP : 6

# 13. .rindex(substring) --> int : returns last index of substring (error if not found)
print(str.rindex("o"))  
# OP : 7


# D. Modification Methods
# 14. .replace(old,new) --> str : replaces substring
print(str.replace("kodle","python"))  
# OP : ayush python

# 15. .strip() --> str : removes whitespace from both ends
print("   hello   ".strip())  
# OP : hello

# 16. .lstrip() --> str : removes whitespace from left
print("   hello   ".lstrip())  
# OP : hello   

# 17. .rstrip() --> str : removes whitespace from right
print("   hello   ".rstrip())  
# OP :    hello

# 18. .removeprefix(prefix) --> str : removes prefix if present
print("Python3".removeprefix("Python"))  
# OP : 3

# 19. .removesuffix(suffix) --> str : removes suffix if present
print("hello.py".removesuffix(".py"))  
# OP : hello


# E. Splitting & Joining Methods
# 20. .split(separator) --> list[str] : splits string into list
print("a,b,c".split(","))  
# OP : ['a','b','c']

# 21. .rsplit(separator) --> list[str] : splits string from right
print("a,b,c".rsplit(",",1))  
# OP : ['a,b','c']

# 22. .splitlines() --> list[str] : splits string at line breaks
print("a\nb\nc".splitlines())  
# OP : ['a','b','c']

# 23. .join(iterable) --> str : joins elements of iterable into string
print("-".join(['ayush','kodle']))  
# OP : ayush-kodle

# 24. .partition(sep) --> tuple : splits at first occurrence
print("ayush-kodle".partition("-"))  
# OP : ('ayush','-','kodle')

# 25. .rpartition(sep) --> tuple : splits at last occurrence
print("ayush-kodle-test".rpartition("-"))  
# OP : ('ayush-kodle','-','test')


# F. Alignment & Padding Methods
# 26. .center(width,fillchar) --> str : centers string
print(str.center(20,"*"))  
# OP : ****ayush kodle****

# 27. .ljust(width,fillchar) --> str : left-justifies string
print(str.ljust(20,"-"))  
# OP : ayush kodle---------

# 28. .rjust(width,fillchar) --> str : right-justifies string
print(str.rjust(20,"-"))  
# OP : ---------ayush kodle

# 29. .zfill(width) --> str : pads with zeros
print("42".zfill(5))  
# OP : 00042


# G. Checking Content Methods
# 30. .isalnum() --> bool : True if string is alphanumeric
print("Hello123".isalnum())  
# OP : True

# 31. .isalpha() --> bool : True if only letters
print("Hello".isalpha())  
# OP : True

# 32. .isdigit() --> bool : True if only digits
print("123".isdigit())  
# OP : True

# 33. .isdecimal() --> bool : True if only decimal digits
print("123".isdecimal())  
# OP : True

# 34. .isnumeric() --> bool : True if numeric (includes fractions etc.)
print("⅔".isnumeric())  
# OP : True

# 35. .isspace() --> bool : True if only spaces
print("   ".isspace())  
# OP : True

# 36. .islower() --> bool : True if all lowercase
print("hello".islower())  
# OP : True

# 37. .isupper() --> bool : True if all uppercase
print("HELLO".isupper())  
# OP : True

# 38. .istitle() --> bool : True if title-cased
print("Hello World".istitle())  
# OP : True

# 39. .isascii() --> bool : True if all characters are ASCII
print("Hello".isascii())  
# OP : True

# 40. .isidentifier() --> bool : True if valid Python identifier
print("my_var".isidentifier())  
# OP : True

# 41. .isprintable() --> bool : True if all characters printable
print("Hello!".isprintable())  
# OP : True


# H. Encoding & Translation Methods
# 42. .encode(encoding) --> bytes : encodes string to bytes
print(str.encode("utf-8"))  
# OP : b'ayush kodle'

# 43. .maketrans(x,y,z) --> dict : creates translation map
table = str.maketrans("abc","123","d")
print(table)  
# OP : {97: 49, 98: 50, 99: 51, 100: None}

# 44. .translate(map) --> str : translates using mapping
print("abcd".translate(table))  
# OP : 123


# I. Formatting Methods
# 45. .expandtabs(tabsize) --> str : replaces tabs with spaces
print("a\tb".expandtabs(4))  
# OP : a   b

# 46. .format(...) --> str : formats string with placeholders
print("My name is {}".format("Ayush"))  
# OP : My name is Ayush

# 47. .format_map(mapping) --> str : formats using dict
print("{name} is {age}".format_map({"name":"Ayush","age":21}))  
# OP : Ayush is 21