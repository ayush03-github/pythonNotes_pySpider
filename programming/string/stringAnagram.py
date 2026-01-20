s1 = "silent"
s2 = "listen"

def string_sorting(s):
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] > s[j]:
                    s[i],s[j] = s[j],s[i]   
        return "".join(s)
        

if string_sorting(list(s1)) == string_sorting(list(s2)):
    print("string is anagram")
else: 
    print("string is not anagram")

    