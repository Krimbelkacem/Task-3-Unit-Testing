import unittest
from tires import CarriganTires  # Import the CarriganTires class from tires.py


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_when_wear_below_threshold(self):
        # Create instance of CarriganTires with tire wear levels below the threshold
        carrigan_tires = CarriganTires()
        # Example tire wear levels below 0.9 threshold
        tire_wear = [0.8, 0.7, 0.6, 0.5]

        # Ensure needs_service returns False when wear is below 0.9 threshold
        self.assertFalse(carrigan_tires.needs_service(tire_wear))

    def test_needs_service_when_wear_above_threshold(self):
        # Create instance of CarriganTires with tire wear levels above the threshold
        carrigan_tires = CarriganTires()
        # Example tire wear levels above or equal to 0.9 threshold
        tire_wear = [0.9, 0.85, 0.95, 0.88]

        # Ensure needs_service returns True when wear is above or equal to 0.9 threshold
        self.assertTrue(carrigan_tires.needs_service(tire_wear))

    def test_needs_service_empty_wear_array(self):
        # Create instance of CarriganTires with an empty tire wear array
        carrigan_tires = CarriganTires()
        tire_wear = []  # Empty tire wear array

        # Ensure needs_service returns False for an empty wear array
        self.assertFalse(carrigan_tires.needs_service(tire_wear))


if __name__ == '__main__':
    unittest.main()
