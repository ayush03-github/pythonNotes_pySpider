# def shiftingValue(str,shift):
#     res = ""
#     for i in str:
#         res += chr(ord(i)+shift)
#     return res

# print(shiftingValue("aSdfg",4))


def shiftingValue(s, shift):
    res = ""

    for ch in s:
        if ch.islower():
            res += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch.isupper():
            res += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            res += ch 

    return res


print(shiftingValue("aSdfgZz", 4))
print(shiftingValue("b", 4))
