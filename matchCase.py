# MatchCase : it is faster way to perform if elif 
# here if a == 1 is written as case 1 and it goes both ways

# NOTE : case values can be integer or float or complex or string or tuple or boolean
# NOTE : case _ must be the last case i.e it should not be defined as first case or middle case
# NOTE : case _ is optional

# SYNTAX:
'''match variableName :
    case condition :
        statement
    case condition :
        statement'''



n = int(input("n: "))
match n :
    case 1 :
        print("monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednesday")
    case 4 :
        print("thursday")
    case 5 :
        print("friday")
    case 6 :
        print("saturday")
    case 7 :
        print("monday")
    case _ :
        print("invalid number of day")


# Print what number of the weeday is the input

n = input("n: ")
match n :
    case "monday" :
        print("1")
    case "tuesday" :
        print("2")
    case "wednesday" :
        print("3")
    case "thursday" :
        print("4")
    case "friday" :
        print("5")
    case "saturday" :
        print("6")
    case "sunday" :
        print("7")
    case _ :
        print("invalid number of day")



    