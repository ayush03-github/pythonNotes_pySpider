fruits = ["apple", "mango", "banana", "papaya"]

print(fruits)
count = 0
while count < len(fruits) :
    print(fruits[count])
    count = count + 1


'''
# Creating a list
my_list = ["apple", "banana", "cherry", 123, True]

# Accessing elements
print(my_list[0])  # Output: apple
print(my_list[-1]) # Output: True
print(my_list[-3])

# Modifying an element
my_list[1] = "orange"
print(my_list) # Output: ['apple', 'orange', 'cherry', 123, True]

# Adding elements
my_list.append("grape") # Adds to the end
my_list.insert(1, "kiwi") # Inserts at a specific index
print(my_list) # Output: ['apple', 'kiwi', 'orange', 'cherry', 123, True, 'grape']

# Removing elements
my_list.remove("cherry") # Removes a specific value
my_list.pop() # Removes the last element
print(my_list) # Output: ['apple', 'kiwi', 'orange', 123, True]

# Getting the length of a list
print(len(my_list)) # Output: 5
'''