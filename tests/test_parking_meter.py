"""Test parking meter validation and purchased time."""
import unittest

from parking_meter import ParkingMeter


class TestParkingMeter(unittest.TestCase):
    """Check meter construction and reassignment."""

    def test_invalid_types_and_setters(self):
        """Reject invalid purchases without replacing a valid value."""
        meter = ParkingMeter(30)
        for bad in (True, False, None, 2.5, "60", -1):
            error = ValueError if type(bad) is int else TypeError
            with self.subTest(value=bad):
                with self.assertRaises(error):
                    ParkingMeter(bad)
                with self.assertRaises(error):
                    meter.minutes_purchased = bad
                self.assertEqual(meter.minutes_purchased, 30)
    def test_valid_construction_and_access(self):
        """Verify valid construction and access."""
        meter = ParkingMeter(60)
        self.assertEqual(meter.minutes_purchased, 60)

    def test_zero_and_positive_minutes_are_valid(self):
        """Verify zero and positive minutes are valid."""
        self.assertEqual(ParkingMeter(0).minutes_purchased, 0)
        self.assertEqual(ParkingMeter(15).minutes_purchased, 15)

    def test_negative_minutes_are_rejected(self):
        """Verify negative minutes are rejected."""
        with self.assertRaises(ValueError):
            ParkingMeter(-1)

    def test_nonnumeric_minutes_are_rejected(self):
        """Verify nonnumeric minutes are rejected."""
        with self.assertRaises(TypeError):
            ParkingMeter("60")

    def test_valid_reassignment(self):
        """Verify valid reassignment."""
        meter = ParkingMeter(30)
        meter.minutes_purchased = 90
        self.assertEqual(meter.minutes_purchased, 90)


if __name__ == "__main__":
    unittest.main()

