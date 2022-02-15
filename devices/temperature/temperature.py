from time import sleep_ms
from devices.settings_for_devices import ds_sensor_ds18x20, roms


def get_temp():
    is_temp = 0
    ds_sensor_ds18x20.convert_temp()
    sleep_ms(700)
    for rom in roms:
        is_temp = ds_sensor_ds18x20.read_temp(rom)
    return is_temp
