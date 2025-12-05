row = int(input("enter number of rows: "))
col = int(input("enter number of columns: "))
val = 1 
for i in range(row):
    for j in range(col):
        print(chr(64 + val), end=" ")
        val +=1
    val =1
    print()