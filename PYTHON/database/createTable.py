import pymysql

try :
    con_obj = pymysql.connect(
        user="root",
        password="Dattebayo@0311",
        host = "127.0.0.1"
    )
    print(con_obj)

    cur_obj = con_obj.cursor()
    cur_obj.execute("create table pybtm.student(name varchar(20), age int (3), username varchar (20), gender varchar (12), marks int (3))")
    print("table created")
except Exception as e :
    print(e)