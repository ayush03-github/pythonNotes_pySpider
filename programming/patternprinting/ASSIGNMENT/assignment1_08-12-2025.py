
n = int(input("enter a number: "))

#         1 
#       2
#     3
#   4
# 5



# val = 1
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             print(val, end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val += 1


#         A 
#       B
#     C
#   D
# E

# val = ord("A")
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             print(chr(val), end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val += 1


#         5 
#       4
#     3
#   2
# 1


# val = n
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             print(val, end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val -= 1


#         Z 
#       Y
#     X
#   W
# V


# val = ord("Z")
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             print(chr(val), end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val -= 1


#         E 
#       D
#     C
#   B
# A

# val = ord("A") + n-1
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             print(chr(val), end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val -= 1



#         1 
#       *
#     2
#   *
# 3


# val = 1
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1 and i % 2 ==0:
#             print(val, end=" ")
#             val += 1
#         elif i+j == n-1 and i % 2 ==1:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()

        # A 
#       A B
#     A B C
#   A B C D
# A B C D E


# for i in range(n):
#     val =ord("A")
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()




#         A 
#       B B
#     C C C
#   D D D D
# E E E E E




# val =ord("A")
# for i in range(n):
    
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
            
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1


#         E 
#       D D
#     C C C
#   B B B B
# A A A A A


# val = ord("A") + n-1
# for i in range(n):
    
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
            
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1


#         E 
#       E D
#     E D C
#   E D C B
# E D C B A



# val = ord("A") + n-1
# for i in range(n):
    
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val = ord("A") + n-1
    

#         Z 
#       Z Y
#     Z Y X
#   Z Y X W
# Z Y X W V

# val = ord("Z")
# for i in range(n):
    
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val = ord("Z")


#         Z 
#       Y Y
#     X X X
#   W W W W
# V V V V V


# val = ord("Z")
# for i in range(n):
    
#     for j in range(n):
#         if i + j >= n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1




#         1 
#       1 2 
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5



# for i in range(n):
#     val=1
#     for j in range(n):
#         if i+j>=n-1:
#             print(val, end=" ")
#             val+=1
#         else:
#             print(" ", end=" ")
#     print()




#         1 
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5

# val=1
# for i in range(n):

#     for j in range(n):
#         if i+j>=n-1:
#             print(val, end=" ")
            
#         else:
#             print(" ", end=" ")
#     print()
#     val+=1


# A B C D E 
#   A B C D 
#     A B C 
#       A B 
#         A


# for i in range(n):
#     val=ord('A')
#     for j in range(n):
#         if(j>=i):
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()


# A B C D E 
#   F G H I
#     J K L
#       M N
#         O


# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if(j>=i):
#             print(chr(val),end=' ')
#             val+=1
#         else:
#             print(' ',end=' ')
#     print()


# 1 1 1 1 1 
#   2 2 2 2
#     3 3 3
#       4 4
#         5


# val=1
# for i in range(n):
#     for j in range(n):
#         if(j>=i):
#             print(val,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val+=1

# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3
#       1 2
#         1

# for i in range(n):
#     val=1
#     for j in range(n):
#         if(j>=i):
#             print(val,end=' ')
#             val+=1 
#         else:
#             print(' ',end=' ')
#     print()

# 5 4 3 2 1 
#   5 4 3 2
#     5 4 3
#       5 4
#         5

# for i in range(n):
#     val=n
#     for j in range(n):
#         if(j>=i):
#             print(val,end=' ')
#             val-=1 
#         else:
#             print(' ',end=' ')
#     print()


# 5 4 3 2 1 
#   5 4 3 2
#     5 4 3
#       5 4
#         5


# val=n+ord('A')-1
# for i in range(n):
#     for j in range(n):
#         if(j>=i):
#             print(chr(val),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#     val-=1 


# E D C B A 
#   E D C B
#     E D C
#       E D
#         E


# for i in range(n):
#     val=n+ord('A')-1
#     for j in range(n):
#         if(j>=i):
#             print(chr(val),end=' ')
#             val-=1 
#         else:
#             print(' ',end=' ')
#     print()