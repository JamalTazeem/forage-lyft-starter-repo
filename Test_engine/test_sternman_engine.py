import unittest
from datetime import date

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):

    def needs_service_True(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def needs_service_False(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
