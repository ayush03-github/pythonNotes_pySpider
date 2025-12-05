row = int(input("enter row number: "))
col = int(input("enter number of columns: "))
val = 1
star = "*"

for i in range(row):
    if i % 2 == 1:
        for j in range(col):
            print(star, end=" ")
    else:
        for k in range(col):
            print(val, end=" ")
        val += 1

    print()




# OR 


# row = int(input("enter row number: "))
# col = int(input("enter number of columns: "))
# val = 1


