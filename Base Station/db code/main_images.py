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
    if timeStr[17] == '0' and timeStr[18] == '0':
        for i in range(0,len(files_paths)):
            image_monitor_db.insertVaribleIntoImageTable('images.db', timeStr[:10], timeStr[11:-14], files_names[i], files_paths[i])
    
    time.sleep(0.5)

# def main():
#     timeStr = terminal_RTC.getTime() # Get current time every second
#     print(timeStr)
#     print("Waiting until next interval")
#     files_names, files_paths = images.getListImageandPath("/home/pi/images/")
#     # String values in timeStr
#     # 18 = 0x seconds
#     # 17 = x0 seconds
#     # 15 = 0x mins
#     # 14 = x0 mins
#     # 12 = 0x hours
#     # 11 = x0 hours
#     if timeStr[17] == '0' and timeStr[18] == '0':
#         for i in range(len(files_paths)):
#             image_monitor_db.insertVaribleIntoImageTable('images.db', timeStr[:9], timeStr[11:-14], files_names[i], files_paths[i])

#     time.sleep(1)

# # Set the interval to 60 seconds (1 minute)
# interval = 60

# # Get the current time
# current_time = time.time()

# # Calculate the next interval time
# next_interval = current_time + interval

# # Loop indefinitely
# while True:
#     # Get the current time
#     current_time = time.time()

#     # Check if it's time for the next interval
#     if current_time >= next_interval:
#         main()

#         # Calculate the next interval time
#         next_interval = current_time + interval
#     else:
#         # Sleep for a short duration before checking again
#         time.sleep(0.1)


while True:
    main()


