from devices.settings_for_devices import *
from devices.LED_with_PWM.LED import led_pwm
from devices.temperature.temperature import get_temp

while True:
    led_pwm()

    if state_ds18x20 is True:
        get_temp()
