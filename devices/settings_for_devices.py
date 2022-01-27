from machine import Pin, I2C, PWM
from devices.clock.ds1307 import DS1307
from devices.temperature import ds18x20, onewire

# Connect DS1307
i2c_rtc_ds1307 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
rtc_1307 = DS1307(i2c_rtc_ds1307)

# Connect DS18b20
ds_pin_ds18x20 = Pin(22)
ds_sensor_ds18x20 = ds18x20.DS18X20(onewire.OneWire(ds_pin_ds18x20))

roms = ds_sensor_ds18x20.scan()
if len(roms) > 0:
    state_ds18x20 = True
    print('Found DS devices: ', roms)
else:
    state_ds18x20 = False
    print('Not found DS devices')

# Connect LED
led = Pin(25)
pwm = PWM(led)
pwm.freq(100000)
