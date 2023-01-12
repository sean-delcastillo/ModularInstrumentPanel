# Modular Instrument Panel

Current State = Unfinished

## Teensy Sketch Generator

---

### Description

Python script that can generate simple sketches for the Teensy development board for use as a USB joystick device from a TOML configuration file.

### Instructions

- Install [Teensy Loader](https://www.pjrc.com/teensy/loaderloader.html)
    - You will need both the loader and a loadersupported Arduino IDE version
    - Setup instructions can be found here:
        - https://www.pjrc.com/teensy/tutorial.html
- Created profiles in TOML format can be found in /profiles/
- Generated sketches are inside /sketches/
- Generate a sketch by invoking the mips script

        python3 mips.py -f test_profile

### TODO
| Status | Task |
|--------|------|
|  TODO  | Test loop for more devices |
|  TODO  | Loop for more devices |
|  TODO  | Upload schematics for panel case |