# IDEA all forcast data gets updated or added into a database.  This will alow for historical data processing and just be cool to have

import sqlite3

def db_connection():
    conn = sqlite3.connect('weather.db')
    print ('Opened database successfully')
    return conn

def db_check(conn):
    conn.execute("""create table if not exists 'forcast' ('id'	INTEGER NOT NULL, 'jsonRaw'	BLOB, PRIMARY KEY('id' AUTOINCREMENT));
    CREATE TABLE "current" ("id"	INTEGER NOT NULL, "temprature"	NUMERIC NOT NULL, "icon"	TEXT NOT NULL, "city"	TEXT NOT NULL, "lat"	TEXT NOT NULL, "longatude"	TEXT NOT NULL, "sunrise"	TEXT NOT NULL, "sunset"	TEXT NOT NULL, "jsonRaw"	BLOB NOT NULL, PRIMARY KEY("id" AUTOINCREMENT))""")

def insert_data():
    conn = db_connection()
    print('im back')
    db_check(conn)
    
if __name__ == '__main__':
    insert_data()