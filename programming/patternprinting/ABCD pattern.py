# row = int(input('how many row: '))
# col = int(input('how many col: '))
# row =4
# col=4
# val =1
# for i in range (row):
#     for j in range (col):
#         print(chr(64+val), end=" ")
#     print() 
#     val += 1






    # OR 
row = int(input("enter row number: "))
col = int(input("enter column number: "))

val = ord('A')
for i in range (row):
    for j in range(col):
        print(chr(val),end=" ")
        val += 1
        if val>ord("Z"):
            val = ord("A")
    print()
    val = ord("A")
    

# and us if to control that using ascii value it does go over z 

    