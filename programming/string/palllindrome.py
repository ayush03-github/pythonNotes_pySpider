str = "malayalam"
str2 = "asdfghjklkjhgfdsa"
s = "racecar"

# temp = s3[::-1]

# if s3 == temp:
#     print("is pallindrome")
# else:
#     print("is not a pallindrome")
j = len(s)-1

for i in range(len(s)):
    if s[i] != s[j]:
        print("not a pallindorme")
        break
    j -= 1
else:
        print("is pallindrome")
    