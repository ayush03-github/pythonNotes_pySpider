n = int(input("n:"))

val = 1
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(val,end=" ")
        val +=1
        if val > 9:
            val = 1
    print()