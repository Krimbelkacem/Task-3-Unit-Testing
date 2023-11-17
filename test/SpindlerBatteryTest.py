import unittest
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_when_required(self):
        # Test if battery needs service when required
        battery = SpindlerBattery(
            last_service_date="2023-01-01", current_date="2023-11-15")
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service_when_not_required(self):
        # Test if battery doesn't need service when it's not required
        battery = SpindlerBattery(
            last_service_date="2023-11-01", current_date="2023-11-15")
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
