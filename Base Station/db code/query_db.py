import sqlite3
import sys
from datetime import datetime

#sys.path.insert(0,'/home/group10/')
#sys.path.insert(0,'/home/group10/sensor_data')


def getAll():
    # Connect to the SQLite database
    conn = sqlite3.connect('sensing.db')
    cursor = conn.cursor()
    print("Successfully connected to sensing.db")

    # Execute the SQL query (Order in descending id order)
    cursor.execute("SELECT * FROM climate ORDER BY id DESC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()
    print("Successfully closed sensing.db")

    # Write the query results to a text file
    with open('allSensorData.txt', 'w') as file:
        for row in rows:
            file.write('|'.join(str(item) for item in row) + '\n')

    print("All sensing data written to allSensorData.txt file.")

def getLast3():
    conn = sqlite3.connect('sensing.db')
    cursor = conn.cursor()
    print("Successfully connected to sensing.db")

    cursor.execute(".headers on")
    cursor.execute(".mode column")
    cursor.execute(".once recentSensorData.txt")
    # Execute the SQL query (Get last 3 entries)
    cursor.execute("SELECT TOP 3 FROM climate ORDER BY id DESC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()
    print("Successfully closed sensing.db")

    # Write the query results to a text file
    with open('recentSensorData.txt', 'w') as file:
        for row in rows:
            file.write('|'.join(str(item) for item in row) + '\n')

    print("Last 3 sensor entires written to recentSensorData.txt file.")




