# MatchCase : it is faster way to perform if elif 
# here if a == 1 is written as case 1

# NOTE : case values can be integer or float or complex or string or tuple or boolean
# NOTE : case _ must be the last case i.e it should not be defined as first case or middle case
# NOTE : case _ is optional


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
    