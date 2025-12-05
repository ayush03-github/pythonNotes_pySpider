# n row and col

# A A A A A
# * * * * *
# B B B B B
# * * * * *

n = int(input("enter a number: "))
# val = ord("A")
# for i in range(n):
#     if i % 2 == 0:
#         for j in range(n):
#             print(chr(val), end=" ")
#         val += 1
#     else:
#         for j in range(n):
#             print("*", end=" ")
#     print()
#______________________________________________________________________________________________________________________________________________



# A * B *
# A * B *
# A * B *
# A * B *





# A * B * C 
# * D * E * 
# F * G * H
# * I * J *

# val = ord("A")
# pos = 1 
# for i in range(n):
#     for j in range(n):
#         if pos % 2 ==1:
#             print(chr(val), end=" ")
#             val+=1
#             if val>ord("Z"):
#                 val = ord("A")
            
#         else :
#             print("*", end=" ")
#         pos += 1

#     print()

# _________________________________________________________________________________________________________________________________________________

# 1 2 3 4
# * * * *
# 5 6 7 8
# * * * *
val = 1
for i in range(n):
    if i %2 == 0:
        for j in range(n):
            print(val, end=" ")
            val+=1
            if val>9:
                val=1
    else:
        for j in range(n):
            print("*", end=" ")
    print()

# _________________________________________________________________________________________________________________________________________________



# 1 * 2 * 3
# * 4 * 5 *
# 6 * 7 * 8
# * 9 * 1 *
# 2 * 3 * 4

# n = int(input("enter a number: "))
# val = 1
# pos = True
# for i in range(n):
#     for j in range(n):
#         if pos:
#             print(val, end=" ")
#             val += 1
#             if val>9:
#                 val=1
#             pos = False
#         else:
#             print("*", end=" ")
#             pos = True

#     print()




