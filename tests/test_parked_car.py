import unittest

from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 30)

    def test_valid_construction_and_properties(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.color, "Blue")
        self.assertEqual(self.car.license_number, "ABC-1234")
        self.assertEqual(self.car.minutes_parked, 30)

    def test_valid_property_reassignment(self):
        self.car.make = "Honda"
        self.car.minutes_parked = 0
        self.assertEqual(self.car.make, "Honda")
        self.assertEqual(self.car.minutes_parked, 0)

    def test_empty_strings_are_rejected(self):
        with self.assertRaises(ValueError):
            self.car.color = ""

    def test_non_string_values_are_rejected(self):
        with self.assertRaises(TypeError):
            self.car.model = 123

    def test_minutes_must_be_nonnegative_integer(self):
        with self.assertRaises(ValueError):
            self.car.minutes_parked = -1
        with self.assertRaises(TypeError):
            self.car.minutes_parked = 1.5


if __name__ == "__main__":
    unittest.main()

