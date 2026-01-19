# program to find first max element along with its index in given list 

# l1 = [1, 3 ,6 ,9, 11, 7 , 11, 4]

# max_element = l1[0]
# index = 0

# for i in range(len(l1)):
#     if max_element < l1[i]:
#         max_element = l1[i]
#         index = i

# print("max element is ", max_element, "on", index,"th index")


# find first two maximum element in the list and display its difference 

l1 = [1, 3 ,6 ,9, 11, 7 , 15, 4]

max1 = l1[0]
max2 = l1[1]

for i in range(len(l1)):
    if max1 < l1[i]:
        max2 = max1
        max1 = l1[i]
    elif max2 < l1[i]:
        max2 = l1[i]
print('difference of both max values is ',max1 - max2)