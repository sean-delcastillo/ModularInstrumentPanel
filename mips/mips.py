"""
Main MIPS script
"""

import subprocess
import serial
import logging

import devicemanager
import parsemanager
import templater

PATH_TO_ARDUINO = "../arduino-1.8.19/"

# TODO Fix serial monitoring function
"""
def monitor_serial():
    with serial.Serial() as ser:
        ser.baudrate = 38400
        ser.port = "/dev/ttyACM0"
        ser.open()
        print(ser.readline())
"""


def main():
    """
    1. Receives CLI arguments
    2. Imports profile toml
    3. Renders sketch from template + profile data
    """


    args = parsemanager.argparse_init()
    file = vars(args)["file"]

    profile = devicemanager.load_profile(file)
    profile_name = profile.get("profile_name")
    is_test = profile.get("profileInfo").get("test")

    device_dictionaries = profile.get("devices")
    device_collection = []
    for device in device_dictionaries:
        device_object = devicemanager.Device(device)
        device_collection.append(device_object)

    rendered_template = templater.render_template(device_collection, is_test)
    templater.save_render(rendered_template, profile_name)

    subprocess.run(PATH_TO_ARDUINO + f"arduino --upload sketches/{profile_name}",shell=True)


if __name__ == "__main__":
    main()
