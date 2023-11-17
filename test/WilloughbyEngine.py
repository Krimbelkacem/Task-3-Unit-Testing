import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_when_required(self):
        # Test if engine needs service when required
        engine = WilloughbyEngine(
            last_service_mileage=5000, current_mileage=7000)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service_when_not_required(self):
        # Test if engine doesn't need service when it's not required
        engine = WilloughbyEngine(
            last_service_mileage=5000, current_mileage=5500)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
