n = int(input("enter a number: "))

for i in range(n-1,-n,-1):
    print(" "*abs(i)+"* "*(n-abs(i)))