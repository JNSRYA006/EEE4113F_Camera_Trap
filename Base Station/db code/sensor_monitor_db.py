# Import appropriate packages
import sqlite3
import sys
import time
from datetime import datetime

sys.path.insert(0,'/home/group10/')
import RTC_setup

sys.path.insert(0,'/home/group10/RTC_SDL_DS3231')
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)

# 'Sensor values' from Sigi
## Get value from .csv file stored on SD card
def getVal(path):
    temp = 25
    humidity = 60
    return temp,humidity

# Returns an object to connect to given database text string
def connectDB(dbName):
    #print "Opened database successfully"
    return sqlite3.connect(dbName)

# Inserts an entry with the following format:
# db: database name (string)
# date: From RTC clock (datetime object)
# temperature: From DHT22 (real)
# humidity: From DHT22 (real)
# dht22 - date = dateitme, dht222 - date = string
def insertEntry(db,tableName,date,temperature,humidity):
    conn = connectDB(db)
    conn.execute("INSERT INTO" + tableName + "(date,temperature,humidity) VALUES ("+ date + "," + temperature + "," + humidity + ")")
    conn.commit()
    print("Successfully wrote to db")
    conn.close()

def insertVaribleIntoTable(db, date, temperature, humidity):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        print("Connected to SQLite Database")

        # sqlite_insert_with_param = """INSERT INTO dht22
        #                   (date, temperature, humidity) 
        #                   VALUES (?, ?, ?);"""

        # data_tuple = (date, temperature, humidity)
        # cursor.execute(sqlite_insert_with_param, data_tuple)
        cursor.execute("INSERT INTO dht22 (date, temperature, humidity) VALUES (?, ?, ?)", (date, temperature, humidity))
        conn.commit()
        print("Python Variables inserted successfully into table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

temperature,humidity = getVal(123)
connectDB('sensorData.db')
#insertEntry('sensorData.db', 'dht22', RTC_setup.getTime, temperature,humidity)
time_datetime = ds3231.read_datetime()
time_datetimeStr = time_datetime.strftime('%Y-%m-%d %H:%M:%S')
insertVaribleIntoTable('sensorData.db', time_datetimeStr, temperature, humidity)
time.sleep(10)

conn = connectDB('sensorData.db')
cursor = conn.execute("SELECT date,temperature,humidity from dht22")
for row in cursor:
    print("Date = " + str(row[0]))
    print("Temp. = " + str(row[1]))
    print("Humidity = " + str(row[2]))

print("Operation done successfully")
conn.close()