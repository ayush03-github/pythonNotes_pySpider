n = int(input("enter a number :"))
count = 0
lc = 0 # it's just to count the loop
for i in range(n,n+1):
    lc += 1 # it's just to count the loop
    if n%i == 0:
        count += 1
        break
if count == 2:
    print(f"{n} is a prime number")
else:
    print(f'{n} is not a prime number')
print(f'loop is running {lc} times') # it's just to count the loop


#  using square root 

n = int(input("enter a number :"))
count = 0
lc = 0 # it's just to count the loop
for i in range(n,n//2+1):
    lc += 1 # it's just to count the loop
    if n%i == 0:
        count += 1
        break
if count == 2:
    print(f"{n} is a prime number")
else:
    print(f'{n} is not a prime number')
print(f'loop is running {lc} times') # it's just to count the loop




