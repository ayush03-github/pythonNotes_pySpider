import math as m
n = int(input("n :"))

for i in range (n):
    print(" "*(n-i-1), end=" ")
    val=1
    for j in range(i+1):
        print(m.comb(i,j), end=" ")
    print()




# for i in range (n):
#     print(" "*(n-i-1), end=" ")
#     val=1
#     for j in range(i+1):
#         print(val,end=" ")
#         val=val*(i-j)//(j+1)
#     print()