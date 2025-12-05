row= int(input("enter no. of rows: "))
col= int(input("enter no. of cols: "))
val= 1
for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()
    val += 1
    if val>9:
        val = 1