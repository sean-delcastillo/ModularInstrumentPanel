"""
Main MIPS script
"""

import logging
import glob
import os

import subprocess
import serial

import devicemanager
import parsemanager
import templater

home = os.getenv("HOME")
PATH_TO_ARDUINO = glob.glob(f"{home}/arduino-*/")[0]


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
    is_test = profile.get("test")

    logging.info("Loading profile: %s", profile_name)
    if is_test is True:
        logging.info("Generating test sketch")
    else:
        logging.info("Generating sketch")

    device_dictionaries = profile.get("devices")
    device_collection = []
    for device in device_dictionaries:
        device_object = devicemanager.Device(device)
        device_collection.append(device_object)

    rendered_template = templater.render_template(device_collection, is_test)
    templater.save_render(rendered_template, profile_name)

    subprocess.run([f"{PATH_TO_ARDUINO}arduino",
                    "--upload",
                    f"sketches/{profile_name}"])


if __name__ == "__main__":
    main()
