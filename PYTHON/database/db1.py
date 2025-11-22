import pymysql

try:
    con_obj = pymysql.connect(
        user = "root",
        password = "Dattebayo@0311",
        host = "127.0.0.1"
    )
    print(con_obj)
except Exception as e:
    print(e)