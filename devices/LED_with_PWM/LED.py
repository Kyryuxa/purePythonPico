from time import sleep
from devices.settings_for_devices import pwm


def led_pwm():
    for duty in range(65025):  # 65636 - full
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
