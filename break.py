# break statement is used to forcefully terminate the loop based on a condition 
# when break executes control comes out of the loop 


'''for i in range(1,11,2):
    if i>=6:
        break
    print(i,end=" ")'''


# NOTE : in case of nested loop break will termionate the immidiate loop where it is present

'''for i in range(1,11):
    for j in range(1,6):
        if j==4:
            break
        print(i,end=" ")'''