a = int(input("a: "))
b = int(input("b: "))

# using temp variable

# temp = a
# a = b
# b = temp
# print(f'swapped value for a is {a} and b is {b}')

# without temp variable

# a = a+b
# b = a - b
# a = a - b

# print(f'swapped value for a is {a} and b is {b}')

# other methods

a, b = b, a

print(f'swapped value for a is {a} and b is {b}')