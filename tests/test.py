import unittest
from unittest.mock import Mock

from mips import devicemanager as dmanager

class TestDeviceManager(unittest.TestCase):
    def test_Device_init_with_empty_dict(self):
        with self.assertRaises(KeyError):
            dmanager.Device({})

    def test_Device_init_with_missing_key(self):
        with self.assertRaises(KeyError):
            dmanager.Device(
                {
                    "device_name": "",
                    "device_type": "",
                    "signal_type": "",
                    "io": ""
                    #, "pin_number": ""
                }
            )
    
    def test_Device_init_with_full_keys(self):
        device = dmanager.Device(
                {
                    "device_name": "",
                    "device_type": "",
                    "signal_type": "",
                    "io": "",
                    "pin_number": ""
                }
            )
        self.assertIsInstance(device, dmanager.Device)