# WAP to encrypt the given string by using foloowing condition
# check the character is uppercase or lowercase
#     if lowercase find its ascii value
#         if ASCII is even add shift value by 3 
#         if it is odd add shift value by 2
#     if it is uppercase find its ASCII value 
#         if it is even add shift value by 5
#         if it is odd add shift value by 4


str = "edrRCBvybBygYyYyhgv"
res = ""
for i in str:
    if i.upper:
        if ord(i)%2 == 0:
            res += chr(ord(i)+5)
        res += chr(ord(i)+4)
    elif i.lower:
        if ord(i)%2 == 0:
            res += chr(ord(i)+3)
        res += chr(ord(i)+2)
print(res)
