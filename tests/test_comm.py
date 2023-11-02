#!/usr/bin/python3
# @Time    : 2023-08-22
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from rms.api import RMS


class TestCommm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rms = RMS("rms_test", "110e9130fdd349ac9475ed18e553ce81", True)

    def test_commm(self):
        data = {
            "salesList": [
                {
                    "salesCode": "SA160120849849924",
                    "storeCode": "E2340000",
                    "SN": "13660/00000001",
                    "salesDate": "2016-11-18 15:31:09 +08"
                }
            ]
        }
        res = self.rms.comm.sign(data)
        self.assertEqual(res, "1DD642B0965AA8B4C55620315E0C1DD3", res)


if __name__ == "__main__":
    unittest.main()
