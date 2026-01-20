# wap to check whether the given string can be a password or not 
# conditions
# length should be greater than 8 and smaller than 30
# it should contain at least one uppercase one lowercase one numeric and one special character

def password(str):
    if len(str) >= 8 and len(str) < 30:
        uc = 0
        lc = 0
        n = 0
        sc = 0
        for i in str:
            if i >= 'A' and i <= 'Z':
                uc += 1
            elif i >= 'a' and i <= 'z':
                lc += 1
            elif i >= "0" and i <= "9":
                n += 1
            else:
                sc +=1
        if uc >= 1 and lc >= 1 and n >= 1 and sc >= 1:
            print("Strong Password")
        else:
            print("weak password")
    else:
        print("length of the password must be atleast 8 characters")
# password("Ayush!123")
password("Ayush123")
# password("ayush!123")
