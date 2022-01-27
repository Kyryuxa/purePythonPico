from devices.LED_with_PWM.LED import led_pwm
from devices.temperature.temperature import get_temp
from devices.clock.initialize_ds1307 import get_time

while True:
    res_temp = get_temp()
    print(f"Temperature: {res_temp}")

    res_time = get_time()
    print(f"Time is: {res_time}")

    led_pwm()
