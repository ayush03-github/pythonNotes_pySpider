import pymysql

try :
    con_obj = pymysql.connect(
        user="root",
        password="Dattebayo@0311",
        host = "127.0.0.1"
    )
    print(con_obj)

    cur_obj = con_obj.cursor()
    if cur_obj.execute("create database pybtm"):
        print("created database pybtm")
    else:
        print("nothing created")

except Exception as e :
    print(e)