import unittest
from unittest.mock import Mock

import mips.devicemanager as dmanager

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

    def test_DeviceCollection_import_devices_method_empty_list(self):
        with self.assertRaises(dmanager.EmptyDeviceCollectionError):
            dmanager.DeviceCollection.import_devices([])
