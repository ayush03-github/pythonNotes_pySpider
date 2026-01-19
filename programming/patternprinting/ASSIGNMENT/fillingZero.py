n = int(input("n: "))
l = len(str(n*n))
val = 1
for i in range(n):
    for j in range(n):
        print(str(val).zfill(l),end=" ")
        val+=1
    print()