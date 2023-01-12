# Modular Instrument Panel

Current State = Unfinished

## Teensy Sketch Generator

### Description

Python script that can generate simple sketches for the Teensy development board for use as a USB joystick device from a TOML configuration file.

### Instructions

- Install [Teensy Loader](https://www.pjrc.com/teensy/loaderloader.html)
    - You will need both the loader and a loadersupported Arduino IDE version
    - Setup instructions can be found in [PJRC's Teensy Tutorial](https://www.pjrc.com/teensy/tutorial.html):
- Create a profile.toml and place it inside the profiles directory
    - Please see the premade test_profile.toml for the toml layout
- Generated sketches are inside sketches directory
- Generate a sketch by invoking the mips.py script

        python3 mips.py -f test_profile

## Dependencies and Modules
- Python
    - [PyTermGUI](https://pypi.org/project/PyTermGUI/)
    - [argparse](https://docs.python.org/3/library/argparse.html)
    - [subprocess](https://docs.python.org/3/library/subprocess.html)
    - [Tomli](https://pypi.org/project/tomli/)

### TODO
| Status | Task |
|--------|------|
|  TODO  | Test loop for more devices |
|  TODO  | Loop for more devices |
|  TODO  | Upload schematics for panel case |
