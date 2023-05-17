# Import appropriate packages
import sqlite3
import sys
from datetime import datetime

sys.path.insert(0,'/home/pi/')
sys.path.insert(0,'/home/pi/sensor_data')

# Inserts an entry with the following format:
# db: database name (string)
# date: From RTC clock (string)
# path: File path (string)
def insertVaribleIntoImageTable(db, date, time, filename, path):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        print("Connected to SQLite Database")

        cursor.execute("INSERT INTO images (date, time, title, path) VALUES (?, ?, ?, ?)", (date, time, filename, path))
        conn.commit()
        print("Image (path) successfully stored into database")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert image into images table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
