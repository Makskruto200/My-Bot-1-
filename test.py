import sqlite3 as sq

with sq.connect("users.db") as con:
        cur=con.cursor()
        a =[i for i in cur.execute("SELECT * FROM users")]
        print(a)
       
           