import sqlite3
con = sqlite3.connect('data/data.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM user where id = 1231")
if cursor.fetchall() == []:
    print(1)

cursor.execute('INSERT INTO status_reg (status) VALUES (?)', ('True'))
con.commit()