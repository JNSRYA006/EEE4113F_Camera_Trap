# Main image storage script

import sys
import time
from datetime import datetime
import time


sys.path.insert(0,'/home/pi/')
import terminal_RTC
import image_monitor_db
import images


def main():
    timeStr = terminal_RTC.getTime() # Get current time every second
    print(timeStr)
    print("Waiting until next interval")
    files_names, files_paths = images.getListImageandPath("/home/pi/images/")
    # String values in timeStr
    # 18 = 0x seconds
    # 17 = x0 seconds
    # 15 = 0x mins
    # 14 = x0 mins
    # 12 = 0x hours
    # 11 = x0 hours
    if timeStr[17] == '0':
        for i in range(0,len(files_paths)):
            image_monitor_db.insertVaribleIntoImageTable('images.db', timeStr[:9], timeStr[11:-14], files_names[i], files_paths[i])
    
    
    time.sleep(0.5)

while True:
    main()


