import unittest

from parking_meter import ParkingMeter


class TestParkingMeter(unittest.TestCase):
    def test_valid_construction_and_access(self):
        meter = ParkingMeter(60)
        self.assertEqual(meter.minutes_purchased, 60)

    def test_zero_and_positive_minutes_are_valid(self):
        self.assertEqual(ParkingMeter(0).minutes_purchased, 0)
        self.assertEqual(ParkingMeter(15).minutes_purchased, 15)

    def test_negative_minutes_are_rejected(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-1)

    def test_nonnumeric_minutes_are_rejected(self):
        with self.assertRaises(TypeError):
            ParkingMeter("60")

    def test_valid_reassignment(self):
        meter = ParkingMeter(30)
        meter.minutes_purchased = 90
        self.assertEqual(meter.minutes_purchased, 90)


if __name__ == "__main__":
    unittest.main()

