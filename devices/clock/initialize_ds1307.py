from machine import I2C
from devices.clock.ds1307 import DS1307
from devices.settings_for_devices import i2c_rtc_ds1307

res = I2C.scan(i2c_rtc_ds1307)
print(res)
rtc = DS1307(i2c_rtc_ds1307)


def init_time():
    year = int(input("Year : "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date : "))
    day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute : "))
    second = int(input("second : "))

    now = (year, month, date, day, hour, minute, second, 0)
    rtc.datetime(now)
    print(rtc.datetime())


def get_time():
    return rtc.datetime()
