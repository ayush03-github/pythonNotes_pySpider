row = int(input("eneter number of rows: "))
col = int(input("enter number of columns: "))
val = 1
for i in range(row):
    for j in range (col):
        print(val, end=" ")
        val+=1
        if val>9:
            val=1
    print()
