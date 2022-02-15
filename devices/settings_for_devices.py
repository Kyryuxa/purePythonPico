from machine import Pin, I2C, PWM
from devices.clock.ds1307 import DS1307
from devices.temperature import ds18x20, onewire

# Connect DS1307
i2c_rtc_ds1307 = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000)
rtc_1307 = DS1307(i2c_rtc_ds1307)

# Connect DS18b20
ds_pin_ds18x20 = Pin(22)
ds_sensor_ds18x20 = ds18x20.DS18X20(onewire.OneWire(ds_pin_ds18x20))
roms = ds_sensor_ds18x20.scan()
print('Found DS devices')

# Connect LED
led = Pin(25)
pwm = PWM(led)
pwm.freq(100000)
