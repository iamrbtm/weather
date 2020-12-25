# IDEA all forcast data gets updated or added into a database.  This will alow for historical data processing and just be cool to have

import sqlite3
import json


def db_connection():
    conn = sqlite3.connect('weather.db')
    print('Opened database successfully')
    return conn


def db_check(conn):
    conn.execute(
        """create table if not exists 'forcast' ('id'	INTEGER NOT NULL, 'UTCdate' TEXT, 'temprature' FLOAT, 'description' TEXT, 'iconpath' TEXT, 'dt_text' DATETIME, "create_timestamp" DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY('id' AUTOINCREMENT));"""
    )

    conn.execute(
        """CREATE TABLE if not exists "current" ("id"	INTEGER NOT NULL, "temprature"	NUMERIC NOT NULL, "icon"	TEXT NOT NULL, "city"	TEXT NOT NULL, "lat"	TEXT NOT NULL, "longatude"	TEXT NOT NULL, "sunrise"	TEXT NOT NULL, "sunset"	TEXT NOT NULL, "current_timestamp"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY("id" AUTOINCREMENT));"""
    )


def insert_data_forcast(UTCdate, temprature, description, iconpath, dt_text):
    conn = db_connection()
    db_check(conn)

    # raw = json.loads(RawJson)
    # strJson = raw.tostring()

    conn.execute("""INSERT INTO forcast ('UTCdate', 'temprature', 'description', 'iconpath', 'dt_text') VALUES (?,?,?,?,?);""",
                 (UTCdate, temprature, description, iconpath, dt_text))

    conn.commit()
    conn.close()


def insert_data_current(temp, icon, city, lat, lon, sunrise, sunset):
    conn = db_connection()
    db_check(conn)
    conn.execute(
        """INSERT INTO 'current' ('temprature', 'icon', 'city', 'lat', 'longatude', 'sunrise', 'sunset') VALUES (?,?,?,?,?,?,?);""", (temp, icon, city, lat, lon, sunrise, sunset))
    conn.commit()
    conn.close()
