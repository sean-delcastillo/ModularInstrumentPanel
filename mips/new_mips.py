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
        self.name = device.get("device_name")
        self.type = device.get("device_type")
        self.signal = device.get("signal_type")
        self.io = device.get("io")
        self.pin_number = device.get("pin_number")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def load_profile(profile: str) -> dict:
    """Creates a profile dictionary from a profiles/profile.toml file"""
    with open(f"profiles/{profile}.toml", "rb") as profile:
        profile_dict = tomli.load(profile)
    return profile_dict

def import_devices(devices: list) -> list:
    """Creates a list of Device objects from a list of device dictionaries"""
    device_list = []
    for device in devices:
        device_list.append(Device(device))
    return device_list

load_profile()