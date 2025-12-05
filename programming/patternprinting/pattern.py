# print("*\n**\n***\n****")
# print("*")

row = int(input('how many row: '))
col = int(input('how many col: '))
for i in range (row):
    for j in range (col):
        print("•", end=" ") # this will print the bullet points equals to the times of col value
    print() # this will shift the cursor to nect row


