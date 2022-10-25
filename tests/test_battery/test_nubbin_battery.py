import imp
import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = date.isoformat("2020-05-15")
        last_service_date = date.isoformat("2016-01-25")
        battery = NubbinBattery(current_date=current_date,
                                last_service_date=last_service_date)
        self.assertTrue(battery.need_service())

    def test_need_service_false(self):
        current_date = date.isoformat("2020-05-15")
        last_service_date = date.isoformat("2019-01-25")
        battery = NubbinBattery(current_date=current_date,
                                last_service_date=last_service_date)
        self.assertTrue(battery.need_service())
