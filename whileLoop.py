#Print 1 to 10 — Use a while loop to print numbers from 1 to 10.

'''num = int(input("Upto which number you want to print number"))
count = 0
while count <= num :
    count = count + 1
    print(count)'''

#  Sum of first N numbers — Take n as input and find the sum from 1 to n.

'''num = int(input("how many output do you want "))
count = 1
total = 0
while count <= num : 
    print ("count is: ", count)
    total = total + count
    count = count + 1
print(total)'''

# Multiplication table — Print the table of a number (input by user) up to 10.

'''num = int(input("n : "))
count = 1
while count <= 10 :
    print(f"{num} x {count} is", count * num)
    count = count + 1'''


# Countdown — Print numbers from input down to 1.

'''n = int(input("n :"))
while n >= 1 :
    print(n)
    n = n -1'''


# List elements — Given a list of fruits, print each fruit on a separate line.

n = int(input("how many fruits do you want : "))


fruits = []
count = 0

while count < n :
    fruit = input(f"Enter the name of fruit {count + 1}: ")
    fruits.append(fruit)
    print(fruits)
    count = count + 1

count = 0
while count < len(fruits) :
    print(fruits[count])
    count += 1
