from datetime import date, datetime
from sqlite3 import Date
import unittest
from carfactory import CarFactory


class AllTest(unittest.TestCase):
    def createCalliope(self):
        temp = Date
        temp.month = temp.month - 1
        CarFactory.create_calliope(date, temp, 23, 40)
        self.assertEqual(CarFactory.create_calliope())
