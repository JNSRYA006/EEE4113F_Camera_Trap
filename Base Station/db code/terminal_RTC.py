# Terminal RTC read
from subprocess import run

def getTime():
    RTC_time_str = run(["sudo","hwclock", "-r"], capture_output=True).stdout
    return RTC_time_str.decode('ASCII')

#print(getTime())
#print(getTime())
#RTC_time_str = run(["sudo","hwclock", "-r"], capture_output=True).stdout
#print(RTC_time_str.decode('ASCII'))