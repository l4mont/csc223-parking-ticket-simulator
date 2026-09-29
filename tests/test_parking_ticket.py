import io
import unittest
from contextlib import redirect_stdout

from parked_car import ParkedCar
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestParkingTicket(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC-1234", 61)
        self.officer = PoliceOfficer("Jordan Lee", "A-1042")

    def test_copies_car_and_officer_information(self):
        ticket = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket.make, "Toyota")
        self.assertEqual(ticket.license_number, "ABC-1234")
        self.assertEqual(ticket.officer_name, "Jordan Lee")
        self.assertEqual(ticket.badge_number, "A-1042")
        self.assertEqual(ticket.illegal_minutes, 1)

    def test_fine_boundaries(self):
        expected = {1: 25, 60: 25, 61: 35, 120: 35, 121: 45}
        for minutes, fine in expected.items():
            with self.subTest(minutes=minutes):
                self.assertEqual(ParkingTicket(self.car, self.officer, minutes).fine, fine)

    def test_invalid_illegal_minutes_are_rejected(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, 1.5)

    def test_report_contains_required_information(self):
        ticket = ParkingTicket(self.car, self.officer, 61)
        output = io.StringIO()
        with redirect_stdout(output):
            print(ticket.get_report())
        report = output.getvalue()
        for value in ("Toyota", "Camry", "Blue", "ABC-1234", "61", "$35.00", "Jordan Lee", "A-1042"):
            self.assertIn(value, report)


if __name__ == "__main__":
    unittest.main()

