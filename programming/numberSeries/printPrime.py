n = int(input("enter a number :"))
for k in range(2,n+1):
    count = 0
    for i in range(n,n//2+1):
        if n%i == 0:
            count += 1
            break
    if count == 0:
        print(k,end=" ")
    