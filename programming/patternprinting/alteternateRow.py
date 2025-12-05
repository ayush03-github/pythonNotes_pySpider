n = int(input("enter a number:"))

val = ord("A")
star = "*"

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(chr(val), end=" ")            
        else:
            print(star, end=" ")
    val += 1
    print()