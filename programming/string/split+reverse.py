s1 = "Bangalore@#$ is%^ a%^& great%^& city@#$%"

s2 = ''

wordList = s1.split()
print(wordList)

for word in wordList:
    count = 0
    for i in word:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            continue
        else:
            count += 1
    if count %2 == 0:
        s2 += word[::-1] + " "
    else:
        s2 += word + " "
print(s2)