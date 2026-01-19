n = int(input("enter a number: "))

# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1, n+1):
#     print("* "*i)

# * * * * * 
#   * * * *
#     * * *
#       * *
#         *

# for i in range(n, 0, -1):
#     print("  "*(n-i) + "* " * i)

# _________________________________________________________________________________________________________________________________________________


# 1
# 2 2
# 3 3 3
# 4 4 4 4


# count = 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(count, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count += 1
# _________________________________________________________________________________________________________________________________________________

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# count = 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(count, end=" ")
#             count += 1
#         else:
#             print(" ", end=" ")
#     count = 1   
#     print()
# _________________________________________________________________________________________________________________________________________________


# 1
# 2 3
# 4 5 6
# 7 8 9 1
# 2 3 4 5 6


# count = 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(count, end=" ")
#             count += 1
#             if count>9:
#                 count =1
#         else:
#             print(" ", end=" ") 
#     print()
# _________________________________________________________________________________________________________________________________________________




# A
# B B
# C C C
# D D D D
# E E E E E


# count = ord("A")
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count += 1
# _________________________________________________________________________________________________________________________________________________


# A
# A B
# A B C
# A B C D
# A B C D E

# count = ord("A")
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#             count += 1
#         else:
#             print(" ", end=" ")
#     count = ord("A")  
#     print()
# _________________________________________________________________________________________________________________________________________________


# A
# B C
# D E F
# G H I J
# K L M N O

# count = ord("A")
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#             count += 1
#             if count>ord("Z"):
#                 count =ord("A")
#         else:
#             print(" ", end=" ") 
#     print()
# _________________________________________________________________________________________________________________________________________________


# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1


# count = n
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(count, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1

# _________________________________________________________________________________________________________________________________________________

# 4       
# 4 3
# 4 3 2
# 4 3 2 1


# count = n
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(count, end=" ")
#             count -= 1
#         else:
#             print(" ", end=" ")
#     count = n   
#     print()

# _________________________________________________________________________________________________________________________________________________

# Z
# Y Y
# X X X
# W W W W
# V V V V V


# count = ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1

# _________________________________________________________________________________________________________________________________________________

# D       
# C C
# B B B
# A A A A

# count = ord("A") + n - 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1

# _________________________________________________________________________________________________________________________________________________


# E
# E D
# E D C
# E D C B
# E D C B A



# count = ord("A") + n - 1
# for i in range(n):
    # for j in range(n):
        # if i >= j:
            # print(chr(count), end=" ")
            # count -= 1
        # else:
            # print(" ", end=" ")
    # print()
    # count = ord("A") + n - 1
#
# _________________________________________________________________________________________________________________________________________________


# E
# D C
# B A E
# D C B A
# E D C B A


# count = ord("A") + n - 1
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print(chr(count), end=" ")
#             count -= 1
#             if count<ord("A"):
#                 count = ord("A") + n - 1
#         else:
#             print(" ", end=" ")
#     print()

#__________________________________________________________________________________________________________________________________________________


# A A A A A 
#   B B B B
#     C C C
#       D D
#         E


# count = ord("A")

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count +=1
#__________________________________________________________________________________________________________________________________________________


# A B C D E 
#   A B C D
#     A B C
#       A B
#         A


# count = ord("A")

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(count), end=" ")
#             count +=1
#         else:
#             print(" ", end=" ")
#     print()
#     count = ord("A")

#__________________________________________________________________________________________________________________________________________________


# 1 1 1 1 1 
#   2 2 2 2
#     3 3 3
#       4 4
#         5


# count = 1

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(count, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count +=1
# _________________________________________________________________________________________________________________________________________________


# 1 2 3 4 
#   1 2 3
#     1 2
#       1


# count = 1

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(count, end=" ")
#             count +=1
#         else:
#             print(" ", end=" ")
#     print()
#     count = 1

#__________________________________________________________________________________________________________________________________________________

# 5 4 3 2 1 
#   5 4 3 2
#     5 4 3
#       5 4
#         5


# count = n

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(count, end=" ")
#             count -=1
#         else:
#             print(" ", end=" ")
#     print()
#     count = n   

#__________________________________________________________________________________________________________________________________________________

# A B C D E 
#   F G H I
#     J K L
#       M N
#         O

# val= ord("A")

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val), end=" ")
#             val += 1
#         else:
#             print(" ",end=" ")
#     print()

# _________________________________________________________________________________________________________________________________________________


# E E E E E 
#   D D D D
#     C C C
#       B B
#         A


# val = ord("A") + n - 1

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val), end=" ")
            
#         else:
#             print(" ", end=" ")
#     print()
#     val-=1
# _________________________________________________________________________________________________________________________________________________


# E D C B A 
#   E D C B
#     E D C
#       E D
#         E


# val = ord("A") + n - 1

# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val), end=" ")
#             val-=1
#         else:
#             print(" ", end=" ")
#     print()
#     val = ord("A") + n - 1
# _________________________________________________________________________________________________________________________________________________

# 1
#   2
#     3
#       4
#         5

# count = 1

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(count, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count += 1


# _________________________________________________________________________________________________________________________________________________

# 5
#   4
#     3
#       2
#         1

# count = n

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(count, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1

# _________________________________________________________________________________________________________________________________________________

# A
#   B
#     C
#       D
#         E

# count = ord("A")

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count += 1
# _________________________________________________________________________________________________________________________________________________

# E
#   D
#     C
#       B
#         A

# count = ord("A") +n-1

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1


# _________________________________________________________________________________________________________________________________________________

# Z
#   Y
#     X
#       W
#         V

# count = ord("Z")

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(chr(count), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     count -= 1


# _________________________________________________________________________________________________________________________________________________

# 1
#   *
#     2
#       *
#         3

# count = 1

# for i in range(n):
#     for j in range(n):
#         if i == j and i % 2 ==0:
#             print(count, end=" ")
#             count += 1
#         elif i==j :
#             print("*", end=" ")
#         elif i>j or i<j:
#             print(" ",end=" ")
#     print()


# _________________________________________________________________________________________________________________________________________________

# * 1 2 3 4 
# 1 * 1 2 3
# 1 2 * 1 2
# 1 2 3 * 1
# 1 2 3 4 *


# rcount = 1
# lcount = 1
# star = "*"

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(star, end=" ")
#         elif i>j:
#             print(lcount,end=" ")
#             lcount += 1
#         elif i<j:
#             print(rcount, end=" ")
#             rcount += 1
#     print()
#     lcount = 1
#     rcount = 1

# OR 


# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print("*", end=" ")
#         elif j < i:
#             print(j + 1, end=" ")
#         else:
#             print(j - i, end=" ")
#     print()

# OR

# for i in range(n):
#     val = 1
#     for j in range(n):
#         if i==j :
#             print("*", end=" ")
#             val=1
#         else:
#             print(val, end=" ")
#             val+=1
#     print()