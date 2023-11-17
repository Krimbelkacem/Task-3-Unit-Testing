import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_when_warning_light_on(self):
        # Test if engine needs service when warning light is on
        engine = SternmanEngine(
            last_service_date="2023-01-01", warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service_when_warning_light_off(self):
        # Test if engine doesn't need service when warning light is off
        engine = SternmanEngine(
            last_service_date="2023-01-01", warning_light_on=False)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
