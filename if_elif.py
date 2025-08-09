'''n = int(input("enter a number : "))
if n==1:
    print("the number is 1")
elif n==2 :
    print("the number is 2")
elif n==3 :
    print("the number is 3")
elif n==4 :
    print("the number is 4")
elif n==5 :
    print("the number is 5")
elif n==6 :
    print("the number is 6")
else :
    print("number is out of range")'''



# ASSIGNMENTS
# WAP to check entered character is upper case alphabet or lowercase alphabet or numeric string

'''n = input("n : ")
# if len(n) != 1 :
#     print("Please enter exactly one character.")
#  add these two commented line because wiothout is numeric we can't write logic for all possible integer
if n >= "A" and n <="Z" :
    print(f"{n} is an upppercase alphabet")
elif n >= "a" and n <= "z" :
    print(f"{n} is a lowercase alphabet")
elif n >= "-9" and n <= "9" :
    print(f"{n} is a numeric string")
else :
    print(f"{n} is invalid")'''

# WAP to check entered integer is positive negative or 0

'''n = int(input("n: "))
if n > 0 :
    print(f"{n} is a positive integer")
elif n < 0 :
    print(f"{n} is a negative integer")
elif n == 0 :
    print(f"{n} is 0")'''

# WAP to check entered number is single digit or two digit or three digit value 

'''n = int(input("n : "))
if (n >= -9 and n <= 9) :
    print(f"{n} is a single digit number")
elif (n >= -99 and n <= -10) or (n >= 10 and n <= 99):
    print(f"{n} is a double")
elif (n >= -999 and n <= -100) or (n >= 100 and n <= 999) :
    print(f"{n} is a triple digit value")'''


# WAP to check entered character is alphabet or numeric string or special character

'''n = input("n : ")
if (n > 'A' and n < 'Z') or (n > 'a' and n < 'z') :
    print(f"{n} is an alphabet")
elif (n >= "-9" and n <= "9") :
    print(f"{n} is a numeric value")
elif ((n > 'A' and n < 'Z') or (n > 'a' and n < 'z') or (n > '-9' and n < '9')) :
    print(f"{n} is an special character")'''



