import sqlite3 as sq

def dobav(id,name,info,foto,numer,sex):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""INSERT INTO users VALUES ("{id}","{name}","{info}","{foto}","{numer}","{sex}")""")
 
def id(id):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""INSERT INTO users (id) VALUES ("{id}")""")
        
def name(id,name):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""UPDATE users SET name=("{name}")WHERE id=("{id}")""")
        
        
def info(id,info):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""UPDATE users SET info=("{info}") WHERE id=("{id}")""")
   
def foto(id,foto):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""UPDATE users SET foto=("{foto}") WHERE id=("{id}")""")
        
   
def numer(id,numer):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""UPDATE users SET numer=("{numer}") WHERE id=("{id}")""")
        
 
def sex(id,sex):
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(f"""UPDATE users SET sex=("{sex}") WHERE id=("{id}")""")
        
 
        
  
        
        
        
  
  
    
    

        

    
    
        
     
        

    