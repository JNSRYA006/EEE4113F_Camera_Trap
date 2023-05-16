# Import appropriate packages
import sqlite3
import sys
import time
from datetime import datetime

sys.path.insert(0,'/home/group10/')
sys.path.insert(0,'/home/group10/sensor_data')

# Returns an object to connect to given database text string
def connectDB(dbName):
    #print "Opened database successfully"
    return sqlite3.connect(dbName)

# Inserts an entry with the following format:
# db: database name (string)
# date: From RTC clock (string)
# temperature: From DHT22 (real)
# humidity: From DHT22 (real)
def insertVaribleIntoSensorTable(db, date, temperature, humidity, light):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        print("Connected to SQLite Database")

        cursor.execute("INSERT INTO climate (date, temperature, humidity, light) VALUES (?, ?, ?, ?)", (date, temperature, humidity, light))
        conn.commit()
        print("Python Variables inserted successfully into table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into climate table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")