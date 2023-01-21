import unittest
from datetime import date

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):

    def needs_service_True(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def needs_service_False(self):
        current_mileage= 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())