print("Choose the gender\nmale\tfemale\tother")
gender = input("enter gender :")
if gender == ["male", "female", "other"] :
    age = int(input("enter age :"))
    if gender == "male" or gender == "other" :
        if (age >= 18 and age <= 65) :
            print("eligible for vote")
        else :
            print("not eligible")
    elif gender == "female":
        if (age >= 21 and age <= 45) :
            print("eligible for vote")
        else :
            print("not eligible")
    else :
        print("invalid gender")
else :
    print("invalid gender")
