str = input("enter the input")

n = len(str)

if len(str)%2 == 1:
    for i in range(n):
        if i == n//2:
            print(s1[j],ends=" ")
        elif j == n//2:
            print(s1[i],ends=" ")
        else:
            print("",ends=" ")

    print()
else:
    print()