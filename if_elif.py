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
# WAP to check entered character is alphabet or numeric string or special character
# WAP to check entered character is upper case alphabet or lowercase alphabet or numeric string
# WAP to check entered integer is positive negative or 0
# WAP to check entered number is single digit or two digit or three digit value 

n = int(input("n : "))
if (n > 'A' and n < 'Z') or (n > 'a' and n < 'z') :
    print(f"{n} is an alphabet")
elif (n > -9 and n < 9) :
    print(f"{n} is a numeric value")
elif ((n > 'A' and n < 'Z') or (n > 'a' and n < 'z') or (n > '-9' and n < '9')) :
    print(f"{n} is an special character")