import unittest
from tires import OctoprimeTires  # Import the OctoprimeTires class from tires.py


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_when_wear_below_threshold(self):
        # Create instance of OctoprimeTires with tire wear levels below the threshold
        octoprime_tires = OctoprimeTires()
        # Example tire wear levels below threshold for sum
        tire_wear = [0.8, 0.7, 0.6, 0.5]

        # Ensure needs_service returns False when sum of wear is below 3
        self.assertFalse(octoprime_tires.needs_service(tire_wear))

    def test_needs_service_when_wear_above_threshold(self):
        # Create instance of OctoprimeTires with tire wear levels above the threshold
        octoprime_tires = OctoprimeTires()
        # Example tire wear levels above or equal to threshold for sum
        tire_wear = [1.2, 0.8, 0.6, 0.5]

        # Ensure needs_service returns True when sum of wear is above or equal to 3
        self.assertTrue(octoprime_tires.needs_service(tire_wear))

    def test_needs_service_empty_wear_array(self):
        # Create instance of OctoprimeTires with an empty tire wear array
        octoprime_tires = OctoprimeTires()
        tire_wear = []  # Empty tire wear array

        # Ensure needs_service returns False for an empty wear array
        self.assertFalse(octoprime_tires.needs_service(tire_wear))


if __name__ == '__main__':
    unittest.main()
