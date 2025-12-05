row = int(input('how many row: '))
col = int(input('how many col: '))
val =1
for i in range (row):
    for j in range (col):
        print(val, end=" ")
        val *= 10
    val = 1
    print()
     
    