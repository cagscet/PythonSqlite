import sqlite3 as sql

def creat_table():
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS KISILER
    id integer PRIMARY KEY,
    name text,
    surname text,
    username text,
    password text,
     """)

    conn.commit()
    conn.close()


def insert(name,surname,username,password):
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    add_command = """INSERT INTO KISILER (name,surname,username,password) VALUES {}"""
    data = (name,surname,username,password)

    cursor.execute(add_command.format(data))
    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    cursor.execute("""SELECT * from KISILER """)
    list_all = cursor.fetchall()

    conn.commit()
    conn.close()

def search(username):
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    search_command = """SELECT * from KISILER WHERE username = '{}' """
    cursor.execute(search_command.format(username))

    user = cursor.fetchone()

    conn.close()
    return user

def update(username,newPassword):
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    update_command = """UPDATE KISILER SET password = '{}' WHERE username ='{}' """
    cursor.execute(update_command.format(newPassword,username))

    conn.commit()
    conn.close()

def delete(username):
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    delete_command = """DELETE from KISILER WHERE username = '{}' """
    cursor.execute(delete_command.format(username))

    conn.commit()
    conn.close()

def table_delete():
    conn = sql.connect('newdata.py')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE KISILER""")

    conn.commit()
    conn.close()
