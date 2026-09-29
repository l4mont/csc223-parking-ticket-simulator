"""Test vehicle properties and validation."""
import unittest

from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    """Check valid and invalid vehicle data."""

    def test_all_string_properties_and_assignments(self):
        """Check every text property during construction and reassignment."""
        fields = ("make", "model", "color", "license_number")
        for field in fields:
            setattr(self.car, field, "Updated")
            self.assertEqual(getattr(self.car, field), "Updated")
            for bad in ("", "   ", None, 123):
                with self.subTest(field=field, value=bad):
                    error = ValueError if isinstance(bad, str) else TypeError
                    with self.assertRaises(error):
                        setattr(self.car, field, bad)
                    values = dict(make="Toyota", model="Camry", color="Blue", license_number="ABC", minutes_parked=0)
                    values[field] = bad
                    with self.assertRaises(error):
                        ParkedCar(**values)

    def test_minutes_types_and_construction(self):
        """Reject invalid minute types and preserve valid values."""
        for bad in (True, False, "30", None, 1.5, -1):
            error = ValueError if type(bad) is int else TypeError
            with self.subTest(value=bad):
                with self.assertRaises(error):
                    ParkedCar("A", "B", "C", "D", bad)
                with self.assertRaises(error):
                    self.car.minutes_parked = bad
        for good in (0, 15):
            self.assertEqual(ParkedCar("A", "B", "C", "D", good).minutes_parked, good)
    def setUp(self):
        """Create fresh objects for each test."""
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 30)

    def test_valid_construction_and_properties(self):
        """Verify valid construction and properties."""
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.color, "Blue")
        self.assertEqual(self.car.license_number, "ABC-1234")
        self.assertEqual(self.car.minutes_parked, 30)

    def test_valid_property_reassignment(self):
        """Verify valid property reassignment."""
        self.car.make = "Honda"
        self.car.minutes_parked = 0
        self.assertEqual(self.car.make, "Honda")
        self.assertEqual(self.car.minutes_parked, 0)

    def test_empty_strings_are_rejected(self):
        """Verify empty strings are rejected."""
        with self.assertRaises(ValueError):
            self.car.color = ""

    def test_non_string_values_are_rejected(self):
        """Verify non string values are rejected."""
        with self.assertRaises(TypeError):
            self.car.model = 123

    def test_minutes_must_be_nonnegative_integer(self):
        """Verify minutes must be nonnegative integer."""
        with self.assertRaises(ValueError):
            self.car.minutes_parked = -1
        with self.assertRaises(TypeError):
            self.car.minutes_parked = 1.5


if __name__ == "__main__":
    unittest.main()

