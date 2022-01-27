from time import sleep_ms, sleep

from devices.settings_for_devices import ds_sensor_ds18x20, roms


def get_temp():
    ds_sensor_ds18x20.convert_temp()
    sleep_ms(750)
    for rom in roms:
        print(rom)
        print(ds_sensor_ds18x20.read_temp(rom))
    sleep(5)
