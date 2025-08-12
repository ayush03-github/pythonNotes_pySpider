# continue statement is used to skip an iteration based on condition.
# when continue excutes control will go back to the loop i.e, the lines below or code below will not be executed

'''for i in range(1,11,1):
    if i == 5: #or we can use other operator so that we can skip more values
        continue
    print(i,end=" ")'''



for i in range(1,11,1):
    if i % 2 == 0 : #or we can use other operator so that we can skip more values like only odd numbers
        continue
    print(i,end=" ")


# NOTE : In case of nested loop CONTINUE will continue the immediate loop where it is present

