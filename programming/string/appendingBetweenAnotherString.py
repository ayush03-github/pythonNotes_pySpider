# str = "moer"
# str2 = "therfuck"
# s3 = ""
# mid = len(str)// 2

# for i in range(len(str)):
#     if i < mid:
#         s3 += str[i]
#     elif i == mid:
#         s3 += str[i]
#         s3 += str2
#     else:
#         s3 += str[i]

# print(s3)


s1 = "moter"
s2 = "herfuck"
mid = len(s1) // 2
if len(s1)%2==0:
    result = s1[:mid] + s2 + s1[mid:]
else:
    result = s1[:mid+1] + s2 + s1[mid+1:]

print(result)