# Modular Instrument Panel

| Status        | Pre-Release  |
| ------------- | ------------ |
| Version       | 0.2.0        |

## Teensy Sketch Generator

### Description

Python script that can generate simple sketches for the Teensy development board for use as a USB joystick device from a TOML configuration file.

### Instructions

- Install [Teensy Loader](https://www.pjrc.com/teensy/loaderloader.html)
    - You will need both the loader and a loadersupported Arduino IDE version
    - Setup instructions can be found in [PJRC's Teensy Tutorial](https://www.pjrc.com/teensy/tutorial.html)
- Install Python requirements from requirements file

        pip install -r requirements

- Create a profile.toml and place it inside the profiles directory
    - Please see the premade test_profile.toml for the toml layout
- Generated sketches are inside sketches directory
- Generate a sketch by invoking the mips.py script

        python3 mips.py -f test_profile

## Packages
- Python
    - [PyTermGUI](https://pypi.org/project/PyTermGUI/)
    - [Tomli](https://pypi.org/project/tomli/)
    - [Jinja2](https://pypi.org/project/Jinja2/)
    - [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html)
    
### Current Features
    1. Basic CLI
    2. Support for devices:
       (*) test only
       - LED*
       - Potentiometer*
       - Button*
    3. Support for modes:
       - N/A
### Features TODO
    1. Terminal User Interface (TUI)
    2. Support for more devices
    3. Support for modes:
       - Joystick
       - Flightsim
