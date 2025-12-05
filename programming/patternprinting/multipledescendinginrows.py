row = int(input('how many row: '))
col = int(input('how many col: '))
val = col
for i in range (row):
    for j in range (col):
        print(val, end=" ")
        val -= 1
    print()
    val = col 
    # val -= 1