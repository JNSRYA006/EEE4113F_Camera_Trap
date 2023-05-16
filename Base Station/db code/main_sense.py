# Test main file to get sensor data
import sys
import sqlite3
import time
from datetime import datetime
import  RPi.GPIO as GPIO
import time
import Adafruit_DHT
import os 


sys.path.insert(0,'/home/group10/')
import terminal_RTC
import return_sense
import sensor_monitor_db


pin_to_circuit = 11

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN=4
Moving_AVG_SIZE = 5
temperature_avg = [None]*Moving_AVG_SIZE
humidity_avg = [None]*Moving_AVG_SIZE

def main():
    timeStr = terminal_RTC.getTime() # Get current time every second
    print(timeStr)
    print("Waiting until next interval")
    # String values in timeStr
    # 18 = 0x seconds
    # 17 = x0 seconds
    # 15 = 0x mins
    # 14 = x0 mins
    # 12 = 0x hours
    # 11 = x0 hours
    if timeStr[17] == '0':
        temperature, humidity, light = return_sense.getSensorVal(pin_to_circuit,DHT_SENSOR,DHT_PIN)
        sensor_monitor_db.insertVaribleIntoSensorTable('sensing.db', timeStr[:-14], temperature, humidity, light)
    
    
    time.sleep(0.5)

while True:
    main()


