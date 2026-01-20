str = "a quick brown fox jumps over a lazy dog"

s2 = set()

for i in str:
    if i == " ":
        continue
    else:
        s2.add(i.lower())

if len(s2) == 26:
    print("is panagram")