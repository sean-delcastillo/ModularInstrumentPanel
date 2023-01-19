"""
Handles devices, profiles and their methods
"""

from dataclasses import dataclass
import tomli

@dataclass(init=False)
class Device:
    """Represents a device that may be connected to the Teensy"""
    name: str
    type: str
    signal: str
    io: str
    pin_number: int

    def __init__(self, device: dict):
        self.name = device["device_name"]
        self.type = device["device_type"]
        self.signal = device["signal_type"]
        self.io = device["io"]
        self.pin_number = device["pin_number"]

def load_profile(profile: str) -> dict:
    """Creates a profile dictionary from a profiles/profile.toml file"""
    with open(f"profiles/{profile}.toml", "rb") as profile_file:
        profile_dict = tomli.load(profile_file)
    return profile_dict
