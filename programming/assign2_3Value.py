n = int(input("enter a number"))

val = 1
p = 1

for i in range(n):
    for j in range(n):
        if p == 1:
            print(val, end=" ")
        elif p == 2:
            print("*", end=" ")
        elif p == 3:
            print(val * 5, end=" ")
    val +=1
    print()