# WAP to mis the given two string in such a way that for the first string need to start form beginning and for the second string need to start from the last
s1 = "auhkde"

s2 = "!lo sy"

temp = ""

for i in range(len(s1)):
    temp += s1[i] + s2[len(s2)-i-1]
print(temp)