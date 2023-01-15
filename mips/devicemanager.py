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

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class EmptyDeviceCollectionError(Exception):
    def __init__(self, devices: list):
        error = f"{devices} list is empty. Device Collection cannot be empty"
        super().__init__(error)

@dataclass
class DeviceCollection:
    """Represents a list of device objects"""
    device: Device

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    def import_devices(devices: list) -> list:
        """Creates a DeviceCollection from a list"""
        device_list = []
        for device in devices:
            device_list.append(Device(device))
        if len(device_list) == 0:
            raise EmptyDeviceCollectionError(devices)
        return device_list

def load_profile(profile: str) -> dict:
    """Creates a profile dictionary from a profiles/profile.toml file"""
    with open(f"profiles/{profile}.toml", "rb") as profile:
        profile_dict = tomli.load(profile)
    return profile_dict

