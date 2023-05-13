## SAVE IN group10 on Pi
import time
import sys
# sys.path is a list of absolute path strings
sys.path.insert(0,'/home/group10/RTC_SDL_DS3231')
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#ds3231.write_all(00,56,19,5,12,5,23)
#ds3231.write_now()

# Returns a datetime value of the current time
def getTime():
    return ds3231.read_datetime()

def getTimeStr():
    return ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")

# Set the time of the RTC Clock
def setTime(seconds,minutes,hours,dayOfWeek,date,month,year):
    ds3231.write_all(seconds,minutes,hours,dayOfWeek,date,month,year)

#print("Ds3231 (getTime)=\t\t%s" + getTime)
print("Ds3231 (getTimeStr) =\t\t%s" + ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S"))