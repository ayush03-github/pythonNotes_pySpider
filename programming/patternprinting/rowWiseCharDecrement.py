row = int(input('how many row: '))
col = int(input('how many col: '))
val = ord("A") + row - 1
if val>ord("Z"):
    val=ord("Z")
for i in range (row):
    for j in range (col):
        print(chr(val), end=" ")
    print()
    val -= 1
    if val<ord("A"):
        val=ord("Z")